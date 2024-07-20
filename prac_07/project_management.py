# project_management.py

"""
Project Management Script
Time Estimate: ~5 hours
"""

from project import Project
import datetime


def display_menu():
    print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- "
          "(A)dd new project\n- (U)pdate project\n- (Q)uit")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
                projects.append(Project(name, start_date, priority, cost_estimate, completion))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    return projects
