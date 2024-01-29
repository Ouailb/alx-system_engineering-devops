#!/usr/bin/python3
"""
Export data to CSV format
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user_info.get('username'),
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })
