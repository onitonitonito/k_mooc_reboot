""" """
class Grade(object):
    def __get__(*args, **kwargs): pass

    def __set__(*args, **kwargs): pass


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40

print(exam.writing_grade)     
