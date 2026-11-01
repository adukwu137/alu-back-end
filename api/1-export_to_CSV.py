#!/usr/bin/python3
"""
A Python script that exports all TODO list tasks for a given employee ID
into a CSV file using standard libraries.
"""

import csv
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
        filename = "{}.csv".format(emp_id)

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(
                f,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                escapechar="\\"
            )
            for task in todos_res:
                writer.writerow([
                    str(emp_id),
                    username,
                    str(task.get("completed")),
                    task.get("title")
                ])
