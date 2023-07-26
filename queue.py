from task import Task

class Queue:
    # every Queue operation (except print) must
    # return a message upon successful execution
    def __init__(self):
        self.queue = []
        self.length = 0

    def print(self):
        # check if empty list
        # loop through the queue list
        # print title and remind_time of each Task object
        # along withh their index in the queue
        for task in self.queue:
            task.print()

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
        # remove and return the front-most item
        # (item is a Task object)
        # decrement length
        pass

if __name__ == '__main__':
    q = Queue()

    q.insert(Task("23:30", "T 1"))
    q.print()
    print()
    q.insert(Task("23:32", "T 2"))
    q.print()
    print()
    q.insert(Task("23:50", "T 3"))
    q.print()
    print()
    q.insert(Task("23:40", "T 4"))
    q.print()
    print()

    q.remove(2).print()
    print()
    q.print()
    print()

    print(Queue().remove(0))
