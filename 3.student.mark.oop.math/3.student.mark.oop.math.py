import student
import course
import mark
import math


# Checking valid type
def validTypeChecking(value, type_name):
    while True:
        try:
            value = int(value)
            if value <= 0 and type_name == "positive_number":  # raise exception for students
                raise ValueError  # Don't need to raise exception <= 0 for course because of DEFAULT
            elif value < 0 or value > 20 and type_name == "mark":  # raise exception for marks
                raise ValueError
            if value is not ValueError:
                return value  # Return value while we don't have exception
        except ValueError:
            if type_name == "positive_number":  # Exception for students
                value = input("Accept only positive integers. Please enter again: ")
            elif type_name == "option":  # Exception for courses
                value = input("No Action! Accept only number 0-8. Please enter again: ")
            elif type_name == "mark":  # Exception for marks
                value = input("Accept only number 0-20. Please enter again: ")


# Checking student
def studentChecking(student_list, student_id):
    for i in range(len(student_list)):
        if student_id in student_list[i].getStudentID():
            print(f"Student ID: \"{student_id}\" already exist!")
            return True
    return False


# Checking course
def courseChecking(course_list, course_id):
    for i in range(len(course_list)):
        if course_id in course_list[i].getCourseID():
            # print(f"Course ID: \"{course_id}\" already exist!")
            return True
    return False


# Input information of students
def studentInfo(num_of_students, student_list):
    if num_of_students == 0:
        print("\n--PLEASE SELECT NUMBER OF STUDENT FIRST!--")
        return
    else:
        for i in range(num_of_students):
            student_id = str(input("\nStudent ID: "))
            while studentChecking(student_list, student_id):  # Input when the student already exist in the list
                student_id = str(input("\nStudent ID: "))
            if not studentChecking(student_list, student_id):
                student_name = str(input("Student Name: "))
                student_dob = str(input("Student DOB:"))
                stu_info = student.Student(student_id, student_name, student_dob)
                student_list.append(stu_info)
        return student_list


# Input course information
def courseInfo(num_of_courses, course_list):
    for i in range(num_of_courses):
        course_id = str(input("\nCourse ID: "))
        while courseChecking(course_list, course_id):  # While True -> course_ID already exist
            course_id = str(input("\nCourse ID: "))
            print(f"Course ID: \"{course_id}\" already exist!")
        if not courseChecking(course_list, course_id):
            course_name = str(input("Course Name: "))
            course_info = course.Course(course_id, course_name)
            course_list.append(course_info)
    return course_list


# Input mark for student in the course
def studentMark(course_list, student_list, mark_dict):
    course_id = str(input("Select Course ID: "))
    while not courseChecking(course_list, course_id):
        if not courseChecking(course_list, course_id):  # if false -> the course does not exist -> create course
            print(f"\nThe course ID \"{course_id}\" is not exist!")
            print("The existed courses:")
            showCourseInfo(course_list)
            create_course = str(input("Do you want to create new course? (Y/N): "))
            if create_course.lower() == "y":
                print("Creating new course...")
                course_list.append(courseInfo(1, course_list))  # create course
            elif create_course.lower() == "n":
                course_id = str(input("\nSelect Course ID: "))
            else:
                print("Invalid choice. Please try again!")
    if len(student_list) == 0:
        print("--THERE ARE NO STUDENTS INFORMATION--")

    else:  # if true -> the course already exist -> can input mark
        mark_dict[course_id] = list()
        for j in range(len(student_list)):
            grade = float(input(f"Name:{student_list[j].getStudentID()} - Enter the mark: "))
            grade = round(validTypeChecking(grade, "mark"), 2)  # Use round function to floor the
            mark_dict[course_id].append(
                mark.Mark(grade, student_list[j].getStudentID(), student_list[j].getStudentName(),
                          student_list[j].getStudentDOB()))
    return mark_dict


# Showing students information
def showStudentInfo(student_list):
    print("\nSTUDENT INFORMATION")
    for i in range(len(student_list)):
        student_id = student_list[i].getStudentID()  # Get student ID
        student_name = student_list[i].getStudentName()  # Get student Name
        student_dob = student_list[i].getStudentDOB()
        print(f"{i + 1}. {student_id} {student_name} {student_dob}")


# Showing course information
def showCourseInfo(course_list):
    if len(course_list) == 0:
        print("-- NO COURSE INFORMATION --")
    else:
        for i in range(len(course_list)):
            course_id = course_list[i].getCourseID()
            course_name = course_list[i].getCourseName()
            print(f"{i + 1}. Course ID: {course_id} - Course Name: {course_name}")


# Showing student marks
def showStudentMark(mark_dict):
    course_id = str(input("Select the course ID: "))
    if course_id in mark_dict:
        for i in range(len(mark_dict[course_id])):
            print(f"ID:{mark_dict[course_id][i].getStudentID()} - Mark:{mark_dict[course_id][i].getMark()}")
    elif course_id not in mark_dict:
        print("The course is not available")


# Main function       
def main():
    num_of_students = 0
    student_list = list()

    num_of_courses = 0
    course_list = list()

    mark_dict = dict()

    while True:
        print("""
            OPTION
            Exit: 0
            Input number of students in class: 1
            Input student information: 2
            Input number of courses: 3
            Input course information: 4
            Select course - Input mark: 5
            Show students list: 6
            Show course list: 7
            Show student marks: 8
            """)
        option = input("Option: ")
        option = validTypeChecking(option, "option")
        match option:
            case 0:
                print("--EXIT THE PROGRAM")
                break
            case 1:
                num_of_students = input("Enter the number of students:")
                num_of_students = validTypeChecking(num_of_students, "positive_number")
            case 2:
                student_list = studentInfo(num_of_students, student_list)
            case 3:
                num_of_courses = input("Enter the number of courses: ")
                num_of_courses = validTypeChecking(num_of_courses, "positive_number")
            case 4:
                course_list = courseInfo(num_of_courses, course_list)
            case 5:
                mark_dict = studentMark(course_list, student_list, mark_dict)
            case 6:
                showStudentInfo(student_list)
            case 7:
                showCourseInfo(course_list)
            case 8:
                showStudentMark(mark_dict)
            case _:
                print("No Action! Please enter an valid option...")


# MAIN
if __name__ == "__main__":
    main()
