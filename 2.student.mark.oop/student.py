class Student:
    def __init__(self, id, name, dob):
        self.__id = id      # set private id
        self.__name = name  # set private name
        self.__dob = dob    # set private dob  
    
    def getStudentID(self):
        return self.__id
    
    def getStudentName(self):
        return self.__name
    
    def getStudentDOB(self):
        return self.__dob


    
