from course import Course
from faculty import Faculty
from timetable import Timetable
from analytics import faculty_workload

# Create Courses
c1 = Course("CS101", "Python", 4)
c2 = Course("CS102", "Data Structures", 3)

# Create Faculty
f1 = Faculty("F01", "Dr. Rao", "CSE")
f2 = Faculty("F02", "Dr. Sharma", "CSE")

# Assign Courses
f1.assign_course(c1)
f2.assign_course(c2)

# Timetable
tt = Timetable()
tt.add_entry("Monday", "9AM", c1, f1)
tt.add_entry("Monday", "11AM", c2, f2)

tt.display()

# Analytics
faculty_workload([f1, f2])
