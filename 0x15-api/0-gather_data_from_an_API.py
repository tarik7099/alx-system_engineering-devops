#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    # Check if the user provides an argument
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name.py> <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    
    # Fetch user information
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    
    # Check if the user ID exists
    if user_response.status_code != 200:
        print("Employee ID not found.")
        sys.exit(1)
    
    employee_name = user_response.json().get('name')

    # Fetch todo list
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    
    # Check if the API request was successful
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list.")
        sys.exit(1)
    
    total_tasks = 0
    completed_tasks = 0

    for task in todos_response.json():
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed_tasks, total_tasks))

    print('\n'.join(["\t " + task.get('title') for task in todos_response.json()
          if task.get('userId') == int(employee_id) and task.get('completed')]))
