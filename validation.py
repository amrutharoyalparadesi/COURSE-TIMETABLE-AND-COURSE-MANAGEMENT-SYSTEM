def validate_course(course_id, name, credits):
    if not course_id or not name:
        raise ValueError("Course ID and Name cannot be empty")
    
    if credits <= 0:
        raise ValueError("Credits must be positive")

def validate_faculty(name):
    if not name:
        raise ValueError("Faculty name cannot be empty")
