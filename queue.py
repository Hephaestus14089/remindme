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
        # check if queue is empty
        # in case of empty queue :-
        # just append the item to the queue list
        # if not empty :-
        # loop through the queue list and
        # compare the remind time
        # of each item in the list
        # with the new Task object
        # put the object at the appropriate position
        # increment length
        self.queue.append(task)

    def remove(self, index):
        # check if index >= queue length
        # find list item if entered index
        # remove list item
        # decrement length
        pass

    def dequeue(self):
        # remove and return the front-most item
        # (item is a Task object)
        # decrement length
        pass

if __name__ == '__main__':
    q = Queue()

    q.insert(Task("1:00", "T 1"))
    q.insert(Task("1:00", "T 2"))
    q.insert(Task("5:00", "T 3"))
    q.insert(Task("11:00", "T 4"))

    q.print()
