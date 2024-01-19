import student
import course
class Mark(student.Student, course.Course):
    # Constructor
    def __init__(self, mark, student_id, student_name, student_DOB):
        self.__mark = mark
        super().__init__(student_id, student_name, student_DOB)
    # Method
    def getMark(self):
        return self.__mark
    
    
