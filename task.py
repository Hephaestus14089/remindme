class Task:
    def __init__(self, remind_time, title="no title"):
        self.title = title
        self.remind_time = remind_time
        self.details = {}

    def update_details_description(self, newVal):
        self.details['description'] = newVal

    def update_details_time(self, timeTuple):
        self.details['start_time'], self.details['end_time'] = timeTuple

    def update_details_start_time(self, newVal):
        self.details['start_time'] = newVal

    def update_details_end_time(self, newVal):
        self.details['end_time'] = newVal

    def update_remind_time(self, newVal):
        self.remind_time = newVal

    def print(self):
        print(f"title: {self.title}")
        print(f"remind_time: {self.remind_time}")

        if self.details:
            print(self.details)

if __name__ == '__main__':
    t1 = Task("2:30", "Title")
    t1.print()
    t1.update_details_description("test description")
    t1.print()
