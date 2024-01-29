#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import json
import urllib.request
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = json.loads(urllib.request.urlopen(f"{base_url}/users/{employee_id}").read().decode("utf-8"))
    todos_data = json.loads(urllib.request.urlopen(f"{base_url}/todos?userId={employee_id}").read().decode("utf-8"))

    total_tasks = len(todos_data)
    done_tasks = [task["title"] for task in todos_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    print(f"Employee {user_data['name']} is done with tasks({num_done_tasks}/{total_tasks}):")
    for title in done_tasks:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    get_employee_todo_progress(int(sys.argv[1]))
