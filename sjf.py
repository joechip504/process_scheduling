# ============================================================================
# Joe Pringle (661114638), CSCI-4210 OpSys, sjf.py
# ============================================================================
import process as pr
from completed_plist import CompletedPlist
import heapq
# ============================================================================


def sjf(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
    """
    TIME, completed, num_processes = -1, 0, len(plist)
    ready_q = []
    running_process, prev_process = None, None
    TIMECS_REMAINING = 0

    p_completed = CompletedPlist()

    while (completed < num_processes):

        TIME += 1

        # handle total wait time for each process
        for p in ready_q:
            p.time_q += 1

        # populate ready_q
        for p in plist:
            if (p.arrived == TIME):
                heapq.heappush(ready_q, p)
                p.arrives(TIME)

        # execute the first process in the ready_q, if one exists
        try:
            if (running_process is None):
                running_process = heapq.heappop(ready_q)

                if(running_process.popped is None):
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
    plist_completed = sjf(plist)
    print()
    plist_completed.statistics()
