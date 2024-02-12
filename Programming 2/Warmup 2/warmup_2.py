from student import Student
from course import Course


def create_students(filename):
    """
    Reads a text file containíng student information, 
    and creates Student-objects based on the contents.
    Name of the file to be read is given as the parameter.
    Each correct row of the file has a name and a student number separated by a slash ('/').
    If a row is correct, a new Student-object is created with that name and student number.
    Incorrect rows, i.e. rows that do not have a string and an integer separated by a slash,
    are skipped.
    Finally the function returns a list of all created Student-objects.
    and (parts[0] is isinstance(parts[0], str)) and (parts[1] is isinstance(parts[1],int))
    """
    list_of_students = []
    file1 = open(filename, "r")
    for line in file1:
        line = line.rstrip()
        parts = line.split("/")
        try:
            parts[1] = int(parts[1])
            if len(parts) == 2:
                a_student = Student(parts[0], parts[1])
                list_of_students.append(a_student)
        except ValueError:
            pass
        except IndexError:
            pass
    file1.close()
    return list_of_students


def add_courses(filename, student):
    """
    Reads a text file containing course information,
    creates Course-objects based on the contents, and adds them
    to the completed courses of the student given as the second parameter.
    Name of the file to be read is given as the first parameter.
    Each correct row of the file has the name of the course and its credits
    separated by a comma (','). Incorrect rows, i.e. rows that do not have a string
    and an integer separated by a comma, are skipped.
    Credits for a course should be in the range 1-15.
    Function returns the amount of courses successfully added for the student.
    """
    success_inc = 0
    file1 = open(filename, "r")
    for line in file1:
        line = line.rstrip()
        parts = line.split(",")
        if (len(parts) == 2) and (1 <= int(parts[1]) <= 15):
            a_course = Course(parts[0], int(parts[1]))
            student.add_course(a_course)
            success_inc += 1
    file1.close()
    return success_inc


def compare_student_numbers(student1, student2):
    """
    Compares two given Student-objects, student1 and student2, and returns the one with a smaller id.

    EXAMPLE:
    given objects:
    student1, id: 123456
    student2, id: 234567

    compare_student_numbers(student1, student2):
    returns: student1
    """
    if student1.get_id() < student2.get_id():
        return student1
    return student2


def get_credits(student):
    """
    Calculates and returns the sum of credits of all the courses the student has completed.
    """
    sum = 0
    courses_of_student = student.get_courses()
    for course in courses_of_student:
        sum += course.get_credits()
    return sum


def compare_credits(student1, student2):
    """
    Compares two students total credits. Returns the student with the highest credit count.
    Use the function get_credits to get the total credits. 
    If both students have an equal amount of credits, the function returns 0.
    """
    credits_student1 = get_credits(student1)
    credits_student2 = get_credits(student2)
    if credits_student1 > credits_student2:
        return student1
    elif credits_student2 > credits_student1:
        return student2
    return 0


def main():
    filename = input("Enter the name of the student file\n")
    student_list = create_students(filename)
    # for student in student_list:
    #     print(student.get_name() + "    " + str(student.get_id()))
    for student in student_list:
        filename = input("Enter the name of the course file\n")
        courses = add_courses(filename, student)
        print("{:d} courses added for {:s}".format(courses, student.get_name()))

    for student in student_list:
        print("{:s} has {:d} credits".format(student.get_name(), get_credits(student)))

    #TODO: Write your own code for testing if the called functions worked

if __name__ == "__main__":
    main()

