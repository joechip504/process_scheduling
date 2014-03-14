import process_sjf as p
import heapq

def sjf(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
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

        # if ready_q empty, can't execute any processes
        except IndexError:
            continue

if __name__ == "__main__":
    plist = p.create_plist() #takes optional argument for num processes
    sjf(plist)
