import process as p
import heapq 

from pprint import pprint

def sjf(plist):
    """
    Shortest Job First (sjf). As processes arrive, execute them in
    increasing order of burst time.
    """
    TIME = 0

    start_time = min( [p.arrived for p in plist] )
    TIME += start_time

    #add starting processes to ready_q
    ready_q = []

    for p in plist:
        if (p.arrived == start_time):
            heapq.heappush(ready_q, p)
            p.arrives(TIME)

if __name__ == "__main__":
    plist = p.create_plist()
    sjf(plist)

