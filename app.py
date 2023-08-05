from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from task_queue import TaskQueue
from timer import Timer
from user_cmd_exec import Interpreter, Executor
import threading
# importing Task is probably unnecessary once Executor is imported
from task import Task

app = Flask(__name__)

task_q = TaskQueue()
timer = Timer(task_q)
executor = Executor(task_q)
interpreter = Interpreter(executor)

# task_q.insert(Task("22:17"))
# timer_thread = threading.Thread(target=timer.start, args=[])
# timer_thread.start()

@app.route('/schedule', methods=['POST'])
def schedule():
    response = MessagingResponse()
    message = Message()

    message.body("Hi")
    response.append(message)

    print(request.form.get('Body'))
    return ""

if __name__ == '__main__':
    app.run()
