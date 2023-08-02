from flask import Flask
from twilio.twiml.messaging_response import Message, MessagingResponse
from task_queue import TaskQueue
from timer import Timer
import threading
# importing Task is probably unnecessary once Executor is imported
from task import Task

app = Flask(__name__)

task_q = TaskQueue()
timer = Timer()

task_q.insert(Task("21:27"))
timer_thread = threading.Thread(target=timer.start, args=[task_q])
timer_thread.start()

@app.route('/schedule', methods=['POST'])
def schedule():
    response = MessagingResponse()
    message = Message()

    message.body("Hi")
    response.append(message)

    print(response)
    return str(response)

if __name__ == '__main__':
    app.run()
