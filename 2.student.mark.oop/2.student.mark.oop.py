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
def studentMark(course_list, student_list, mark_dict):
    course_id = str(input("Enter Course ID: "))    
    for i in range(len(course_list)):
        if course_id == course_list[i].getCourseID(): # check that the course_id in the course_list or not
            mark_dict[course_id] = list()                     
            for j in range(len(student_list)):
                grade = float(input(f"Name:{student_list[j].getStudentID()} - Enter the mark: "))
                mark_dict[course_id].append(mark.Mark(grade, student_list[j].getStudentID(), student_list[j].getStudentName(), student_list[j].getStudentDOB()))
            return mark_dict
        elif course_id != course_list[i].getCourseID() and i == len(course_list) -1:
            print("The course is not avaiable")
    
    

# Showing students information
def showStudentInfo(num_of_students, student_list):
    print("\nSTUDENT INFORMATION")
    for i in range(num_of_students):
        student_id = student_list[i].getStudentID() # Get student ID
        student_name = student_list[i].getStudentName() # Get student Name
        student_dob = student_list[i].getStudentDOB()
        print(f"{i+1}. {student_id} {student_name} {student_dob}")

# Showing course information
def showCourseInfo(num_of_courses, course_list):
    for i in range(num_of_courses):
        course_id = course_list[i].getCourseID()
        course_name = course_list[i].getCourseName()
        print(f"{i+1}. Course ID: {course_id} - Course Name: {course_name}")
        
# Showing student marks
def showStudentMark(mark_dict):
    course_id = str(input("Select the course ID: "))
    if course_id in mark_dict:
        for i in range(len(mark_dict[course_id])):
            print(f"ID:{mark_dict[course_id][i].getStudentID()} - Mark:{mark_dict[course_id][i].getMark()}" )
    elif course_id not in mark_dict :
        print("The course is not avaiable")
    

# Main function       
def main():
    num_of_students = 0
    student_list = list()
    
    num_of_courses = 0
    course_list = list()
    
    mark_dict = dict()
    
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
                mark_dict = studentMark(course_list, student_list, mark_dict)
            case 6:
                showStudentInfo(num_of_students, student_list)
            case 7:
                showCourseInfo(num_of_courses, course_list)
            case 8:
                showStudentMark(mark_dict)
            case _ :
                print("No Action!")
            

#MAIN      
if __name__ == "__main__":
    main()