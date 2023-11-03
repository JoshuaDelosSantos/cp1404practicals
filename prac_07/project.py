"""
prac_07 - project.py

Estimated time: 60 mins
Actual time: 10 mins
"""

import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of data for Project."""
        return (
            f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}"
            f", completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Determine if a Project is < other Project based on priority."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Determine if a Project is equal to other Project based on priority."""
        return self.priority == other.priority

    def __gt__(self, other):
        """Determine if a Project is > other Project based on priority."""
        return self.priority > other.priority

    def is_complete(self):
        """Determine if instance is complete based on percentage."""
        return self.completion_percentage == 100
