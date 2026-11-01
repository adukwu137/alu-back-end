#!/usr/bin/python3
"""
A Python script that returns an employee's TODO list progress
using a REST API based on their employee ID.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]

        users_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

        user_res = requests.get(users_url).json()
        todos_res = requests.get(todos_url).json()

        employee_name = user_res.get("name")
        total_tasks = len(todos_res)

        done_tasks = [task for task in todos_res if task.get("completed") is True]
        number_of_done_tasks = len(done_tasks)

        print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task.get('title')}")
