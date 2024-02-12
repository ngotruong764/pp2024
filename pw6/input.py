from domains import mark
from domains import course
import output as op
import math
import os
import zipfile
import pickle


# Checking valid type
def validTypeChecking(value, type_name):
    while True:
        try:
            if type_name != "mark":  # Assign type
                value = int(value)
            else:
                value = float(value)
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
def courseChecking(course_list, course_id, option='b'):  # option == r: retrieve course object
    for i in range(len(course_list)):  # option == n: return boolean
        if course_id in course_list[i].getCourseID():
            if option == "r":
                return course_list[i]
            else:
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
                stu_info = mark.Mark(student_id, student_name, student_dob)  # Student infor object
                student_list.append(stu_info)
                # writeToFile("students.txt", stu_info)
        return student_list


# Input course information
def courseInfo(num_of_courses, course_list):
    for i in range(num_of_courses):
        course_id = str(input("\nCourse ID: "))
        while courseChecking(course_list, course_id):  # While True -> course_ID already exist
            course_id = str(input("\nCourse ID: "))  # -> Enter new course_ID
            print(f"Course ID: \"{course_id}\" already exist!")
        if not courseChecking(course_list, course_id):
            course_name = str(input("Course Name: "))
            course_credit = input("Course Credit:")
            course_credit = validTypeChecking(course_credit, "positive_number")  # Check the validity of credit
            course_info = course.Course(course_id, course_name, course_credit)
            course_list.append(course_info)
            # writeToFile("courses.txt", course_info)
    return course_list


# Input student mark
def studentMark(course_list, student_list):
    course_id = str(input("Select Course ID: "))
    while not courseChecking(course_list, course_id):  # if false -> the course does not exist -> create course
        print(f"\nThe course ID \"{course_id}\" is not exist!")
        print("The existed courses:")
        op.showCourseInfo(course_list)
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
        # input student
        for i in range(len(student_list)):
            grade = float(input(f"Name:{student_list[i].getStudentID()} - Enter the mark: "))
            grade = round(validTypeChecking(math.floor(grade * 10) / 10, "mark"), 1)  # Use floor method to floor the
            student_list[i].setMark(str(course_id), grade)
            # writeToFile("marks.txt", student_list[i])
    return student_list


# Write object to file
def writeToFile(file_name, lst):
    with open(file_name, 'ab') as file:
        for i in range(len(lst)):
            pickle.dump(lst[i], file)


# Read object from file
def readFile(file_name):
    lst = []
    try:
        with open(file_name, 'rb') as file:
            while True:
                value = pickle.load(file)
                lst.append(value)
    except EOFError:
        return lst


# Delete file
def deleteFile(file_name):
    os.remove(file_name)


# Compress file
def compress_to_dat(files, output_file):
    with zipfile.ZipFile(output_file, 'w') as zf:
        for file in files:
            zf.write(file)


# Decompress file
def decompressFile(decompressed_file):
    if os.path.isfile(decompressed_file):
        option = str(input(f"Do you want to decompress the {decompressed_file} (Y/N):"))
        if option.lower() == "y":
            with zipfile.ZipFile(decompressed_file, 'r') as unzip:
                unzip.extractall(".")  # . is current directory
            print(f"Decompressed file {decompressed_file} has been successfully.")
            return True  # True = decompress
        return False
    else:
        print(f"The file {decompressed_file} does not exist.")
        return False    # False = no action
