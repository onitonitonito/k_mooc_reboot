""" '퍼블릭' / '프라이빗' / '시크릿' 매서드가 존재하는가? NO! / 맹글링? """
# - '파이썬' 은 퍼블릭 매서드만 존재함 = '양식' 있는 다 큰 어른
# - '맹글링' mangling 은 같은 '매서드'명의 중복방지.. 사용 '프라이빗' 아님

import _script_run_utf8
_script_run_utf8.main()


class ManOne(object):
    def __init__(self, kind):
        self.kind = kind

    def __eat_food_on(self):
        print("'%s'... 식탁에서 접시에 먹는다" % self.kind)


class DogOne(ManOne):               # 이유는 알 수 없지만 '상속'받음~!! -.-;;;
    def __eat_food_on(self):
        print("'%s'... 개밥그릇에 먹는다" % self.kind)


m1 = ManOne('사람')
d1 = DogOne('개')

""" 개밥을 식탁에서 먹을 수는 없을까?? : (일반 매서드) """
# m1.eat_food_on()
# d1.eat_food_on()

""" 맹글링: '더블언더스코어' 로 개밥을 식탁에서~!"""
d1._DogOne__eat_food_on()
d1._ManOne__eat_food_on()           # '사람'의 방식으로 먹는다.

""" 그럼? 사람은 개밥그릇에 먹을 수도 있나 ?? *ㅁ*;;;;; """
# m1._DogOne__eat_food_on()         # 'ManOne' object has no attribute
# 어이쿠~... 자식 매서드를 불러올수 없네~.. ㅠㅜ;;;;
