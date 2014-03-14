import process_sjf_preemption as p
import heapq

def preempts(running_process, ready_q):
    """
    Peek at the top of the ready_q. If a process in the ready_q
    has less time remaining than the current process, return 
    TRUE. Else, return FALSE.
    """
    try:
        return ready_q[0] < running_process

    except:
        return False

def sjf_preemption(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time. If a process arrives with lower remaining
    time than the current process, run it immediately.
    """
    TIME, completed, num_processes = -1, 0, len(plist)
    ready_q = []
    running_process = None

    while (completed < num_processes):

        TIME += 1

        # populate ready_q
        for p in plist:
            if (p.arrived == TIME):
                heapq.heappush(ready_q, p)
                p.arrives(TIME)

        # execute the first process in the ready_q, if one exists
        try:
            if (running_process is None):
                running_process = heapq.heappop(ready_q)

                if (running_process.popped == None):
                    running_process.popped = TIME

        # if ready_q empty, can't execute any processes
        except IndexError:
            continue

        # If a preemption occurs, print a message indicating a context switch.
        # Then, switch the current process with the one on top of the heap
        if preempts( running_process, ready_q ):
            running_process.switches(ready_q[0], TIME)
            heapq.heappush( ready_q, running_process )
            running_process = heapq.heappop(ready_q)

            if (running_process.popped is None):
                running_process.popped = TIME

        if (running_process.is_complete()):
            running_process.completes(TIME)
            completed += 1
            running_process = None

        else:
            running_process.time -= 1

        #handle total wait time for each process
        for p in ready_q:
            p.time_q += 1


if __name__ == "__main__":
    plist = p.create_plist() #takes optional argument for num processes
    sjf_preemption(plist)
