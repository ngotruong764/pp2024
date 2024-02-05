import numpy as np


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
            course_credit = course_list[i].getCourseCredit()
            print(f"{i + 1}. Course ID: {course_id} - Course Name: {course_name} - Course Credit: {course_credit}")


# Showing student marks
def showStudentMark(student_list):
    course_id = str(input("Select the course ID: "))
    for i in range(len(student_list)):
        if student_list[i].getMark(course_id) is not None:
            print(f"Student ID:{student_list[i].getStudentID()} - Mark:{student_list[i].getMark(course_id)}")
        else:
            print("The course is not available")
            break


def sortMarks(student_list, sort_option):
    temp_mark_list = np.array([], dtype=[('Student ID', 'U100'), ('Mark', 'U100')])
    for i in range(len(student_list)):
        if student_list[i].getMark("GPA") is not None:  # Retrieve student mark into list
            student_temp_mark = np.array([(student_list[i].getStudentID(), student_list[i].getMark("GPA"))],
                                         dtype=temp_mark_list.dtype)
            temp_mark_list = np.append(temp_mark_list, student_temp_mark)
    temp_mark_list = np.sort(temp_mark_list)  # Sorting ascending
    if sort_option == "2":  # 0 sort for descending
        temp_mark_list = temp_mark_list[-1::-1]  # slicing array
    showAverageGPA(temp_mark_list)


# Calculate average GPA
def calAverageGPA(course_list, student_list):
    # Option
    print("""ALL: calculate average GPA of all courses
    Single course: calculate average GPA of course
    0: Terminate and Calculate""")

    course_id = str(input("Select Course ID: "))
    if course_id.lower() == "all":  # Calculate average mark for all course
        for i in range(len(student_list)):
            total_grade = 0
            total_credit = 0
            for j in range(len(course_list)):
                grade = student_list[i].getMark(course_list[j].getCourseID())
                if grade is not None:
                    total_grade += grade * course_list[j].getCourseCredit()
                    total_credit += course_list[j].getCourseCredit()
            average_gpq = round(total_grade / total_credit, 2)  # Calculate average GPA
            student_list[i].setMark("GPA", average_gpq)
            print(f"{student_list[i].getStudentID()}: {average_gpq}")

        sort_decision = input("Do you want to sort GPA? (y/n): ")
        if sort_decision.lower() == "y":
            print("1: Ascending GPA\n2: Descending")
            sort_option = input("Sort option: ")
            sortMarks(student_list, sort_option)


def showAverageGPA(mark_list):
    for i in range(len(mark_list)):
        print(f"Student ID: {mark_list[i]['Student ID']} - GPA:{mark_list[i]['Mark']}")
