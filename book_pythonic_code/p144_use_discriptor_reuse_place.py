""" BETTER WAY-31: Use Discriptor than reusing @property
    """

class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = ValueError


galileo = Homework()
galileo.grade = 95

romeo = Homework()
# romeo.grade = -10           # ValueError: Grade must be between 0 and 100

class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
# -------------------------------------
    @property
    def writing_Grade(self):
        return self._writing_grade

    @writing_Grade.setter
    def writing_Grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

# ------------------------------------- REPEATEDLY USE - NO GOOD.
    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value
