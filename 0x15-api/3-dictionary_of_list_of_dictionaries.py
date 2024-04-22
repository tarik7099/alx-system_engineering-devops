#!/usr/bin/python3
"""
Exports to-do list information for all employees to JSON format.

This script fetches to-do list information for all employees and exports
it to a JSON file in the required format.
"""

import json
import requests


def export_todo_all_employees():
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users = requests.get(base_url + "users").json()

    # Dictionary to store all tasks for all users
    all_tasks = {}

    # Iterate over each user
    for user in users:
        user_id = str(user['id'])
        username = user['username']

        # Fetch the to-do list for the user
        todos = requests.get(
            base_url + "todos",
            params={"userId": user_id}
        ).json()

        # List to store tasks for the current user
        user_tasks = []

        # Iterate over each task for the user
        for todo in todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task)

        # Add tasks for the current user to the dictionary
        all_tasks[user_id] = user_tasks

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)


if __name__ == "__main__":
    export_todo_all_employees()
