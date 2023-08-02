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
        reminder_str = task_obj.title
        reminder_details_str = task_obj.export_details_str()
        if reminder_details_str != "":
            reminder_str += "\n\n" + reminder_details_str
        self.dispatch_message(reminder_str)

    def dispatch_schedule(self, schedule_tup, index_needed = True, details_needed = False):
        schedule_str = ""

        if len(schedule_tup) == 0:
            schedule_str = "TaskQueue empty!"
        else:
            for i in range(len(schedule_tup)):
                task = schedule_tup[i]
                if index_needed:
                    schedule_str += f"Index: {i}\n"
                schedule_str += task.export_task_str(details_needed)
                schedule_str += "\n"

        self.dispatch_message(schedule_str)

if __name__ == "__main__":
    Dispatcher().dispatch_message("Test Dispatcher class.")
