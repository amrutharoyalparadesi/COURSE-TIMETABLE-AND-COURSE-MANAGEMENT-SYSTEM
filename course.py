class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def display(self):
        return f"{self.course_id} - {self.name} ({self.credits} credits)"
