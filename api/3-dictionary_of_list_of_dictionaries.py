#!/usr/bin/python3
"""
A Python script that exports all TODO list tasks for all employees
into a JSON file using standard libraries.
"""

import json
import urllib.request


if __name__ == "__main__":
    u_url = "https://jsonplaceholder.typicode.com/users"
    t_url = "https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(u_url) as response:
        users_res = json.loads(response.read().decode())

    with urllib.request.urlopen(t_url) as response:
        todos_res = json.loads(response.read().decode())

    # Map user IDs to their usernames
    user_dict = {user.get("id"): user.get("username") for user in users_res}

    all_tasks_dict = {}

    for user_id, username in user_dict.items():
        user_tasks = []
        for task in todos_res:
            if task.get("userId") == user_id:
                task_info = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_info)
        all_tasks_dict[str(user_id)] = user_tasks

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_tasks_dict, f)
