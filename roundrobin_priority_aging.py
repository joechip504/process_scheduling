# ============================================================================
# Joe Pringle (661114638), CSCI-4210 OpSys, roundrobin_priority_aging.py
# ============================================================================
import process_priority as pr
from completed_plist import CompletedPlist

"""Configurable time slice defaulted to 100ms"""
TIME_SLICE = 100

# Time for context switch, TCS. Instructions said to include this, but
# this should not be modified, since 7ms removing old process and 10ms
# selecting and resuming new process was not specified to be adjustable.
TCS = 17


def ages(running_process, TIME):
    """
    Returns True if a process has waited in the ready_q for 
    1000ms. Called every time TIME is incremented, for correctness.
    """
    return (running_process.time_q > 1000 and
            running_process.time_q % 1000 == 0)


def preempts(running_process, ready_q):
    """
    Peek at the top of the ready_q. If a process in the ready_q
    has less time remaining than the current process, return 
    TRUE. Else, return FALSE.
    """
    try:
        return ready_q[0].priority < running_process.priority

    except:
        return False


def roundrobin_priority_aging(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
    """
    TIME, completed, num_processes = -1, 0, len(plist)
    ready_q = []
    running_process, prev_process = None, None
    TIMECS_REMAINING = 0
    TIMERR_REMAINING = 0
    p_completed = CompletedPlist()

    while (completed < num_processes):

        TIME += 1
        TIMERR_REMAINING -= 1

        # Due to aging, using a heap to maintain order isn't as
        # effective. We'll just sort by priority each iteration.

        for p in ready_q:
            if(ages(p, TIME)):
                p.ages(TIME)

        ready_q.sort()

        # handle total wait time for each process
        for p in ready_q:
            p.time_q += 1

        # populate ready_q
        for p in plist:
            if (p.arrived == TIME):
                ready_q.append(p)
                ready_q.sort()
                p.arrives(TIME)

        # execute the first process in the ready_q, if one exists
        try:
            if (running_process is None):
                TIMERR_REMAINING = TIME_SLICE

                running_process = ready_q.pop(0)
                if (running_process.popped is None):
                    running_process.popped = TIME

                # indicate a context switch. 10 ms to select and resume
                # the new process
                pr.switches(prev_process, running_process, TIME)
                TIMECS_REMAINING += 10

        # if ready_q empty, can't execute any processes
        except IndexError:
            if (TIMECS_REMAINING == 0):
                prev_process = None
            continue

        # if a context switch is occurring, wait until it finishes
        if (TIMECS_REMAINING > 0):
            TIMECS_REMAINING -= 1
            continue

        # if the time slice is complete, indicate a context switch, put
        # the current process at the end of the ready_q, and grab another
        # process out of the ready_q
        if (TIMERR_REMAINING == 0):
            ready_q.append(running_process)
            ready_q.sort()
            pr.switches(running_process, ready_q[0], TIME)

            prev_process = running_process
            running_process = ready_q.pop(0)

            if (running_process.popped is None):
                running_process.popped = TIME

            TIMERR_REMAINING = TIME_SLICE
            TIMECS_REMAINING += TCS

        # If a preemption occurs, print a message indicating a context switch.
        # Then, switch the current process with the one on top of the heap
        ready_q.sort()

        if preempts(running_process, ready_q):
            prev_process = running_process
            pr.switches(running_process, ready_q[0], TIME)

            ready_q.append(running_process)
            ready_q.sort()
            running_process = ready_q.pop(0)

            if (running_process.popped is None):
                running_process.popped = TIME

        if (running_process.is_complete()):

            running_process.completes(TIME)
            p_completed.push(running_process)
            completed += 1

            # we will not check for a context switch until the
            # next iteration, decrement time. this way, a context switch will
            # begin immediately as a process completes
            TIME -= 1

            # 7 ms in context switch to clear old process
            prev_process = running_process
            TIMECS_REMAINING += 7
            running_process = None

        else:
            running_process.time -= 1

    return p_completed

if __name__ == "__main__":
    plist = pr.create_plist()  # takes optional argument for num processes
    plist_completed = roundrobin_priority_aging(plist)
    print()
    plist_completed.statistics()
