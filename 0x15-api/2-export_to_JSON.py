#!/usr/bin/python3
"""
Get all data for a specific user ID
"""
import json
import requests
from sys import argv

def get_user_data(user_id):
    user_info = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()

    user_data = {
        "user_id": user_id,
        "username": user_info.get("username"),
        "tasks": tasks
    }

    return user_data

if __name__ == "__main__":
    user_id = argv[1]
    user_data = get_user_data(user_id)

    with open(f"{user_id}_all_data.json", "w", encoding='utf-8') as jsonfile:
        json.dump(user_data, jsonfile, ensure_ascii=False, indent=4)
