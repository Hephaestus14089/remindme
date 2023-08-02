from datetime import datetime
import time
from task import Task
from task_queue import TaskQueue
from dispatcher import Dispatcher

# the number of seconds to sleep could be user specifiable
# note: we do not need a Timer instance when queue is empty

class Timer:
    def __init__(self):
        self.dispatcher = Dispatcher()

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
                self.dispatcher.dispatch_reminder(q.dequeue())

            time.sleep(10)
        # the timer is theoritically dead as soon as the above while loop is exited
        print("Timer stopped.")

if __name__ == "__main__":
    timer = Timer()
    q = TaskQueue()

    q.insert(Task("20:28", "T 1"))
    # q.insert(Task("16:43", "T 2"))
    # q.insert(Task("16:50", "T 3"))
    # q.insert(Task("16:40", "T 4"))

    timer.start(q)
