# project.py

from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority

