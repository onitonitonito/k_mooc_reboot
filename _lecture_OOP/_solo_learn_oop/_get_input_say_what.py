""" 이것은 비비 꼬인 코드 """

# 중요하지 않은 '사소'한 함수는 '람다'로 대치합니다.
# def say(noun):
#     return 'You said "{}"'.format(noun)

# 명령어의 매서드 목록(DICT)
VERB_DICT = {
    "say": (lambda x: print("You said '%s' \n\n" % x)),
    "sing": (lambda x: print("I can't sing '%s'..Sorry \n\n" % x)),
    }

def get_input():
    input_str = input("입력값 = {명령어} {명령}: ")
    commands = input_str.split()
    verb = commands[0]              # {명령어}

    if verb in VERB_DICT:           # {명령어}가 목록에 있다면.
        user_func = VERB_DICT[verb] # 목록의 실행함수()를 가져온다.
    else:
        print("알수 없는 명령어: '{}'". format(verb))
        print("you can use : %s \n\n" % list(VERB_DICT.keys()))
        return                      # 함수() 탈출하면 재실행 됨(= continue)

    if len(commands) >= 2:          # {명령어}에 인자가 1개 이상 있다면..
        args = commands[1:]         # followed - args 'str', : 'HELLO?'
        user_func(*args)
    else:
        user_func("nothing")        # You said 'nothing'




if __name__ == '__main__':
    while True:
        get_input()



""" 실행결과
입력값 = {명령어} {명령}: tt
알수 없는 명령어: 'tt'
you can use : ['say', 'sing']

입력값 = {명령어} {명령}: sing hole
I can't sing 'hole'..Sorry

입력값 = {명령어} {명령}: say HELLO~!
You said 'HELLO~!'
"""
