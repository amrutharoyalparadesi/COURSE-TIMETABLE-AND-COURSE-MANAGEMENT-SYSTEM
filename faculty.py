class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def display(self):
        courses = [c.name for c in self.assigned_courses]
        return f"{self.name} ({self.department}) -> {courses}"
