import student
import course
import mark

# Input information of students
def studentInfo(num_of_students, student_list):
    if num_of_students == 0:
        print("\n--THERE ARE NO STUDENT!--")
        return 
    else:
        for i in range(num_of_students):
            student_id = str(input("\nStudent ID: "))
            student_name = str(input("Student Name: "))
            student_dob = str(input("Student DOB:"))
            stu_info = student.Student(student_id, student_name, student_dob)
            student_list.append(stu_info)
        return student_list

# Input course information
def courseInfo(num_of_courses, course_list):
    for i in range(num_of_courses):
        course_id = str(input("\nCourse ID: "))
        course_name = str(input("Course Name: "))
        course_info = course.Course(course_id, course_name)
        course_list.append(course_info)
    return course_list

#Input mark for student in the course
def studentMark(course_list, student_list, mark_list):
    course_id = str(input("Enter Course ID: "))    
    if course_id == course_list[0].getCourseID(): #fix line 31 32 33
        mark_list.append(course_id)                            
        for i in range(len(student_list)):
            grade = float(input(f"{student_list[i].getStudentID()}Enter the mark: "))
            input_grade = mark.Mark(grade) # input grade
            mark_list[student_list[i].getStudentID()] =  input_grade.getMark()
        return mark_list
    else:
        print("The course is not avaiable")
    
    

# Showing students information
def showStudentInfo(num_of_students, student_list):
    print("\nSTUDENT INFORMATION")
    for i in range(num_of_students):
        student_id = student_list[i].getStudentID() # Get student ID
        student_name = student_list[i].getStudentName() # Get student Name
        student_dob = student_list[i].getStudentDOB()
        print(f"{i+1} {student_id} {student_name} {student_dob}")

# Showing course information
def showCourseInfo(num_of_courses, course_list):
    for i in range(num_of_courses):
        course_id = course_list[i].getCourseID()
        course_name = course_list[i].getCourseName()
        print(f"{i+1}. Course ID: {course_id} - Course Name: {course_name}")

# Main function       
def main():
    num_of_students = 0
    student_list = list()
    
    num_of_courses = 0
    course_list = list()
    
    mark_list = list()
    
    while(True):
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
        option = int(input("Option: "))
        match option:
            case 0:
                print("--EXIT THE PROGRAM")
                break
            case 1:
                num_of_students = int(input("Enter the number of students:"))
            case 2:
                student_list = studentInfo(num_of_students, student_list)
            case 3:
                num_of_courses = int(input("Enter the number of courses: "))
            case 4:
                course_list = courseInfo(num_of_courses, course_list)
            case 5:
                mark_list = studentMark(course_list, student_list, mark_list)
            case 6:
                showStudentInfo(num_of_students, student_list)
            case 7:
                showCourseInfo(num_of_courses, course_list)
                

#MAIN      
if __name__ == "__main__":
    main()