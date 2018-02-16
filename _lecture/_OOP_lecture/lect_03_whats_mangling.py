import _script_run_utf8
_script_run_utf8.main()

class ManOne(object):
    def __eat_food_on(self):
        print('식탁에서 접시에 먹는다')

class DogOne(ManOne):               # 이유는 알 수 없지만 '상속'받음~!!
    def __eat_food_on(self):
        print('개밥그릇에 먹는다')

m1 = ManOne()
d1 = DogOne()

""" 개밥을 식탁에서 먹을 수는 없을까?? """
# m1.eat_food_on()
# d1.eat_food_on()

""" 맹글링: '더블언더스코어' 로 개밥을 식탁에서~!"""
d1._DogOne__eat_food_on()
d1._ManOne__eat_food_on()

""" 그럼? 사람은 개밥그릇에 먹을 수도 있나 ?? *ㅁ*;;;;; """
# m1._DogOne__eat_food_on() # 'ManOne' object has no attribute
# 자식 매서드를 불러올수 없네~.. ㅠㅜ;;;;
