"""
prac_06 - programming_language.py

Estimated time: 30 mins
Actual time:
"""


class ProgrammingLanguage:
    """Represent a programming language object"""
    def __init__(self, field="", typing="", reflection=True, year=0):
        """Initialise programming language instance"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamically typed"""
        pass
