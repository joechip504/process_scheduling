import process as p
import heapq 

from pprint import pprint

def sjf(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
    """
    ready_q = []
    completed = 0
    TIME = 0

    while (completed < len(plist) ):

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

      
          

if __name__ == "__main__":
    plist = p.create_plist()
    sjf(plist)

