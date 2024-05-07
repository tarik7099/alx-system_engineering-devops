#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user_info = requests.get(base_url + "users/{}".format(employee_id)).json()
    username = user_info.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(base_url + "todos", params).json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    # Write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
