import process as p
import heapq 


def update_plist(time, ready_q):
    """creates a new plist without processes at 'time'""" 
    return [p for p in ready_q if (p.arrived != time)]


def sjf(plist):

    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
    """

    num_processes = len(plist)
    ready_q = []
    completed = 0
    TIME = -1 
    running_process = None 

    while (completed < num_processes ):

        TIME += 1

        #populate ready_q
        for p in plist:
            if (p.arrived == TIME):
                heapq.heappush(ready_q, p)
                p.arrives(TIME)

        #execute the first process in the ready_q, if one exists
        try:
            if (running_process is None):
                running_process = heapq.heappop(ready_q)

            if (running_process.is_complete()):
                running_process.completes(TIME)
                completed += 1
                running_process = None

            else:
                running_process.time -= 1

        #if ready_q empty, can't execute any processes 
        except IndexError:
            continue

if __name__ == "__main__":
    plist = p.create_plist()
    sjf(plist)

