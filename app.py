from flask import Flask
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello world!</p>"

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
