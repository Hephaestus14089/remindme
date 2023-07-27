from datetime import datetime
from queue import Queue
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
