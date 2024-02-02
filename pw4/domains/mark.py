import numpy as np
from pw4.domains import student
from pw4.domains import course


class Mark(student.Student, course.Course):
    # Constructor
    def __init__(self, student_id, student_name, student_dob):
        # self.mark_arr = np.empty(shape=0, dtype={"course_id", "dob":float})
        self.mark_arr = np.array([], dtype=[('course_id', 'U100'), ('mark', float)])
        super().__init__(student_id, student_name, student_dob)

    # Method
    def setMark(self, course_id, mark):
        new_mark = np.array([(course_id, mark)], dtype=self.mark_arr.dtype)
        self.mark_arr = np.append(self.mark_arr, new_mark)

    def getMark(self, course_id):
        boolean_mask = self.mark_arr['course_id'] == course_id  # boolean indexing array
        if np.any(boolean_mask):
            return self.mark_arr[boolean_mask]['mark'][0]
        else:
            return None
