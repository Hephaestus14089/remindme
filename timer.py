from datetime import datetime
import time
from queue import Queue
from task import Task
# import dispatcher

# the number of seconds to sleep could be user specifiable
# note: we do not need a Timer instance when queue is empty

class Timer:
    def get_curr_datetime():
        return { # convert str to int and then again to str
            'time': ':'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().time()).split(':')[:2]))))),
            'date': '-'.join(list(map(lambda x: str(x), list(map(lambda x: int(x), str(datetime.now().date()).split('-'))))))
        }
        # note:
        # the final int to str conversion might not be needed
        # if the Task objects remind_time dictionary has int values

    def start(self, q):
        while True:
            if q.isEmpty():
                break

            curr = Timer.get_curr_datetime() # dictionary containing current datetime
            remind_time = q.peek().remind_time

            if curr['date'] == remind_time['date'] and curr['time'] == remind_time['time']:
                print("Dispatch!") # dummy dispatch
                q.dequeue() # the return object to be dispatched

            time.sleep(10)
        print("Timer stopped.")

if __name__ == "__main__":
    timer = Timer()
    q = Queue()

    q.insert(Task("12:3", "T 1"))
    q.insert(Task("00:46", "T 2"))
    q.insert(Task("00:47", "T 3"))
    q.insert(Task("00:48", "T 4"))

    timer.start(q)
