class Course:
    # Constructor
    def __init__(self, course_id, course_name, credit):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credit = credit

    # Method
    def getCourseID(self):
        return self.__course_id

    def getCourseName(self):
        return self.__course_name

    def getCourseCredit(self):
        return self.__credit
