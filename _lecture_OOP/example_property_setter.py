"""
# [파이썬] get/set 속성값과 프로퍼티(property)
# https://whatisthenext.tistory.com/115
"""
# print(__doc__)


class Movie:
    def __init__(self, movie_name):
        # hidden
        self.__before_name = ""
        self.__movie_name = movie_name

    @property
    def movie_name(self):
        # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋습니다.
        return self.__movie_name

    @movie_name.setter
    def movie_name(self, new_movie_name):
        """ 영화를 변경하는 setter 메서드"""
        # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋습니다.
        self.__before_name , self.__movie_name = self.__movie_name, new_movie_name

        echoes = [
            f"== CHANGE PROPERTY BY SETTER ==",
            f" - BEFORE: {self.__before_name}",
            f" - AFTER : {self.movie_name}",
            f"................................",
            f"",
        ]

        [print(echo) for echo in echoes]



mv = Movie('Super Man')

print(mv.movie_name == mv._Movie__movie_name, mv.movie_name)

funcs = [func
        for func in mv.__dir__()
        if func.startswith("_")
        ]

mv.movie_name = 'Spider Man'
print(mv.movie_name == mv._Movie__movie_name, mv.movie_name)


mv._Movie__movie_name = "Iron Man"
mv.movie_name = "Iron Man"
print("... Touched Secret Variable directly! w/o setter ...")
print(mv.movie_name == mv._Movie__movie_name, mv.movie_name)

print(f" - BEFORE: {mv._Movie__before_name}")
print(f" - AFTER : {mv._Movie__movie_name}")
