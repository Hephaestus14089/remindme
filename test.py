#!/usr/bin/env python3
from task import *

def test_task():
    t1 = Task("2:30")
    t1.print()

    t1.update_title("title_test")
    t1.update_remind_time("3:30")
    t1.update_details_description("test description")
    t1.update_details_time(("4:00PM", "6:00PM"))
    t1.print()

    t1.update_title("")
    t1.update_details_start_time("5:00")
    t1.update_details_end_time("")
    t1.print()

    t1.update_remind_time("")
    t1.update_details_time(("", ""))
    t1.print()

if __name__ == '__main__':
    test_task()
