import process as p
import heapq 

from pprint import pprint

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
    TIME = 0

    while (completed < num_processes ):

        #execute the first process in the ready_q, if there is one
        try:
            p = heapq.heappop(ready_q)
            TIME += p.time
            p.completes(TIME)
            completed += 1

        #else, populate the ready_q
        except IndexError:
            start_time = min( [p.arrived for p in plist] )
            for p in plist:
                if (p.arrived == start_time):
                    heapq.heappush(ready_q, p)
                    p.arrives(TIME)

            plist = update_plist(start_time, plist)

      
          

if __name__ == "__main__":
    plist = p.create_plist()
    sjf(plist)

