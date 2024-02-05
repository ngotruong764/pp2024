import input as ip
import output as op


# Main function
def main():
    num_of_students = 0
    student_list = list()

    num_of_courses = 0
    course_list = list()

    while True:
        print("""
            OPTION
            Exit: 0
            Input number of students in class: 1
            Input student information: 2
            Input number of courses: 3
            Input course information: 4
            Select course - Input mark: 5
            Calculate average GPA: 6
            Show students list: 7
            Show course list: 8
            Show student marks: 9
            """)
        option = input("Option: ")
        option = ip.validTypeChecking(option, "option")
        match option:
            case 0:
                ip.deleteFile("students.txt")
                ip.deleteFile("courses.txt")
                ip.deleteFile("marks.txt")
                print("--EXIT THE PROGRAM")
                break
            case 1:
                num_of_students = input("Enter the number of students:")
                num_of_students = ip.validTypeChecking(num_of_students, "positive_number")
            case 2:
                student_list = ip.studentInfo(num_of_students, student_list)
            case 3:
                num_of_courses = input("Enter the number of courses: ")
                num_of_courses = ip.validTypeChecking(num_of_courses, "positive_number")
            case 4:
                course_list = ip.courseInfo(num_of_courses, course_list)
            case 5:
                student_list = ip.studentMark(course_list, student_list)
            case 6:
                op.calAverageGPA(course_list, student_list)
            case 7:
                op.showStudentInfo(student_list)
            case 8:
                op.showCourseInfo(course_list)
            case 9:
                op.showStudentMark(student_list)
            case _:
                print("No Action! Please enter an valid option...")


# MAIN
if __name__ == "__main__":
    main()
