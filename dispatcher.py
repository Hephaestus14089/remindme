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

        if 'description' in task_obj.details:
            print(task_obj.details)
            reminder_str += "\n\n" + task_obj.details['description']

        if 'start_time' in task_obj.details or 'end_time' in task_obj.details:
            reminder_str += "\n\nEvent timings :-"
            if 'start_time' in task_obj.details:
                reminder_str += "\nstart: " + task_obj.details['start_time']
            if 'end_time' in task_obj.details:
                reminder_str += "\nend: " + task_obj.details['end_time']

        self.dispatch_message(reminder_str)

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
