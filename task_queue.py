from task import Task
from dispatcher import Dispatcher

class TaskQueue:
    # every TaskQueue operation (except print) must
    # return a message upon successful execution
    def __init__(self):
        self.queue = []
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def export_schedule_tuple(self):
        return tuple(self.queue)

    def insert(self, task):
        if self.length != 0:
            for i in range(self.length):
                if task.compare_remind_time(self.queue[i]) < 0:
                    self.queue.insert(i, task)
                    self.length += 1
                    return
        # if queue empty or cannot be inserted in the middle
        # just insert it at the end
        self.queue.append(task)
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return None
        for i in range(self.length):
            if i == index:
                taskObj = self.queue[i]
                del self.queue[i]
                self.length -= 1
        return taskObj

    def dequeue(self):
        return self.remove(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

if __name__ == '__main__':
    q = TaskQueue()

    q.insert(Task("9:30 PM", "T 1"))
    q.insert(Task("9:32 PM", "T 2"))
    q.insert(Task("9:50 PM", "T 3"))
    q.insert(Task("9:40 PM", "T 4"))

    print(q.export_schedule_tuple())

    Dispatcher().dispatch_schedule(q.export_schedule_tuple())
