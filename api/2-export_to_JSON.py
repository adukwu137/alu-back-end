#!/usr/bin/python3
"""
A Python script that exports all TODO list tasks for a given employee ID
into a JSON file using standard libraries.
"""

import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]

        u_url = "https://jsonplaceholder.typicode.com/users/{}"
        t_url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        users_url = u_url.format(emp_id)
        todos_url = t_url.format(emp_id)

        with urllib.request.urlopen(users_url) as response:
            user_res = json.loads(response.read().decode())

        with urllib.request.urlopen(todos_url) as response:
            todos_res = json.loads(response.read().decode())

        username = user_res.get("username")
        filename = "{}.json".format(emp_id)

        task_list = []
        for task in todos_res:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            task_list.append(task_dict)

        data = {str(emp_id): task_list}

        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(data, f)
