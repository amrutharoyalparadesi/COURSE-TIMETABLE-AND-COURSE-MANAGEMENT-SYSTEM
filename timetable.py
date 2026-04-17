class Timetable:
    def __init__(self):
        self.schedule = {}

    def add_entry(self, day, time_slot, course, faculty):
        key = (day, time_slot)

        if key in self.schedule:
            raise Exception("⚠️ Clash detected!")

        self.schedule[key] = (course, faculty)

    def display(self):
        for key, value in self.schedule.items():
            day, time = key
            course, faculty = value
            print(f"{day} {time} -> {course.name} by {faculty.name}")
