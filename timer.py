from datetime import datetime
import time
from queue import Queue
from task import Task
# import dispatcher

# Timer instance :-
# every 30s, refreshes current time and date
# and checks with the remind_time of the first queue element
# if match found, dequeues and passes the Task object to the dispatcher

# infinite loop
# sleep for 30s
# refresh current time
# check current time with the remind time of the first Task object in the queue
# if matches call dispatcher and pass the Task object

# note: we do not need a Timer instance when queue is empty

class Timer:
    def __init__(self):
        pass

    def get_curr_datetime():
        # convert str to int and then again to str
        return {
            'time': ':'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().time()).split(':')[:2]))))),
            'date': '-'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().date()).split('-'))))))
        }

    def start(self, q):
        while True:
            if q.isEmpty():
                break

            curr = Timer.get_curr_datetime() # dictionary containing current datetime
            remind_time = q.peek().remind_time

            print(curr, remind_time)

            if curr['date'] == remind_time['date'] and curr['time'] == remind_time['time']:
                print("Dispatch!") # dummy dispatch
                q.dequeue() # the return object to be dispatched

            time.sleep(10)

if __name__ == "__main__":
    timer = Timer()

    q = Queue()

    q.insert(Task("00:45", "T 1"))
    q.insert(Task("00:46", "T 2"))
    q.insert(Task("00:47", "T 3"))
    q.insert(Task("00:48", "T 4"))

    timer.start(q)
