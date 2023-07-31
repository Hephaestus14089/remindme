from dotenv import load_dotenv
import os
from twilio.rest import Client

class Dispatcher:
    def __init__(self):
        load_dotenv()
        # fetch necessary environment variables
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        # create Twilio Client for this object
        self.client = Client(account_sid, auth_token)

    def dispatch_message(self, message_body):
        self.client.messages.create(
            from_=f"whatsapp:{os.getenv('TWILIO_PHONE_NUMBER')}",
            body=f"{message_body}",
            to=f"whatsapp:{os.getenv('RECEIVER_PHONE_NUMBER')}"
        )

    def dispatch_reminder(self, task_obj):
        # accept a Task object
        # create the reminder message
        # dispatch the message
        pass

    def dispatch_schedule(self, schedule_tup):
        schedule_str = ""

        if len(schedule_tup) == 0:
            schedule_str = "TaskQueue empty!"
        else:
            for i in range(len(schedule_tup)):
                task = schedule_tup[i]
                schedule_str += f"Index: {i}\n"
                schedule_str += f"Remind time: {task.remind_time}\n"
                schedule_str += f"Title: {task.title}\n"
                schedule_str += "\n"

        self.dispatch_message(schedule_str)

if __name__ == "__main__":
    Dispatcher().dispatch_message("Test Dispatcher class.")
