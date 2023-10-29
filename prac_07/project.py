"""
prac_07 - project.py

Estimated time: 60 mins
Actual time:
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of data for Project."""
        return (
            f"{self.name}, start:{self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}"
            f", completion: {self.completion_percentage}%")

    def is_complete(self):
        return self.completion_percentage == 100
