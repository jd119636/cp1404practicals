class Project:
    """Represent a single project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name} | {self.start_date} | priority {self.priority} | ${self.cost_estimate:,.2f} | {self.completion}% complete"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion >= 100