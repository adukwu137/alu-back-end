#!/usr/bin/python3
"""
A Python script that returns an employee's TODO list progress
using urllib based on their employee ID.
"""

import sys
import json
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        
        users_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)

        # Fetch user data
        with urllib.request.urlopen(users_url) as response:
            user_res = json.loads(response.read().decode())

        # Fetch todos data
        with urllib.request.urlopen(todos_url) as response:
            todos_res = json.loads(response.read().decode())

        employee_name = user_res.get("name")
        total_tasks = len(todos_res)
        
        done_tasks = [task for task in todos_res if task.get("completed") is True]
        number_of_done_tasks = len(done_tasks)

        print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name, number_of_done_tasks, total_tasks
            )
        )
        for task in done_tasks:
            print("\t {}".format(task.get('title')))
