#FUNCTION   
    # Input information of students
def studentInfo(numOfStudents):
    if numOfStudents == 0:
        print("\n--THERE ARE NO STUDENT!--")
        return 
    else:
        studentDict = dict()
        for i in range(numOfStudents):
            studentID = str(input("Enter the ID of student: "))
            studentName = str(input("Enter the name of student: "))
            dob = str(input("Enter thr DOB of student: "))
            studentDict[studentID] =dict()       # Create 2D dictionary
            studentDict[studentID]["Name"] = studentName
            studentDict[studentID]["DOB"] = dob
            print("\n")
        return studentDict
   
    # Input information of courses
def courseInfo(numberOfCourses, courseDict):
    courseDict = dict()
    for i in range(numberOfCourses):
       courseID = str(input("Enter the course ID: "))
       courseName = str(input("Enter the couse name: "))
       courseDict[courseID] = courseName
       print("\n")
    return courseDict

    # Input mark for students in the course
def studentMark(studentDict, courseList, markDict):
    courseID = str(input("Select course ID: "))
    if courseID in courseList:
        markDict[courseID] = dict()
        for studentID in studentDict.keys():
            mark = float(input(f"{studentID} Mark: "))
            markDict[courseID][studentID] = mark
        return markDict
    else:
        print("The course is not available")
        
      
    # Print the list of students
def showStudentInfo(studentDict):
    print("\nSTUDENT INFORMATION")
    idx = 1
    for studentID, info in studentDict.items():
        print(f"{idx}. {studentID:<8} {info['Name']} {info['DOB']:<8}")
        idx += 1
        
    #Print the list of courses
def showCourse(courseDict):
    print("\nCOURSE INFORMATION")
    for courseID, courseName in courseDict.items():
        print(f"ID:{courseID} - Name:{courseName}")
    
    #Print student marks for a given course  
def showStudentMarks(studentDict, markDict):
    queryCourseID = str(input("Select course ID: "))
    if queryCourseID in markDict :
        print(f"\nSTUDENT MARKS OF {queryCourseID} COURSE")
        for studentID, mark in markDict[queryCourseID].items():
            print(f"ID:{studentID} - Mark:{mark}" ) # modify this
    else:
        print("The course is not available")

       
#MAIN
def main():
    studentDict = dict() # Empty student dict
    courseDict = dict() # Empty course list
    markDict = dict()   # Empty mark list
    numOfStudents = 0   
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
        option = int(input("\nOption: "))
        # Menu action
        match option: 
            case 0:
                print("--EXIT THE PROGRAM--")
                break
            case 1:   # Input number of students
                numOfStudents = int(input("Enter the number of students: "))
            case 2:   # Input information of student
                studentDict = studentInfo(numOfStudents)
            case 3:   # Input number of courses
                numOfCourses = int(input("Enter the number of courses: "))
            case 4:   #Input course information
                courseDict = courseInfo(numOfCourses, courseDict)
            case 5:   #Input mark
                markDict = studentMark(studentDict, courseDict, markDict)
                print(f"marlist {markDict}")
            case 6:   #Show student information
                showStudentInfo(studentDict)
            case 7:   #Show student course
                showCourse(courseDict)
            case 8:   #Show student marks
                showStudentMarks(studentDict, markDict)

if __name__ == '__main__':
    main()