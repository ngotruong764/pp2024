import student
import course
class Mark(course.Course, student.Student):
    def __init__(self, mark):
        self.__mark = mark
    def getMark(self):
        return self.__mark
        
        
