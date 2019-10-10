""" 백준-1927 최소합 문제 (파이썬3.6)

# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
# x가 0이면 배열에서 가장 작은 값 출력, 그 값을 배열에서 제거하는 경우.
# 입력 되는 자연수는 2^31 (214,7483,648) 보다 작다.

"""

# heapq 도큐멘테이션 : https://docs.python.org/3.6/library/heapq.html
# This module provides an implementation of the heap queue algorithm,
# also known as the priority queue algorithm.

import os
import sys
import heapq

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)

# script_run 한글 출력을 위한 문장 / IDE터미널을 쓰면 한글 문제 O.K
import script_run
script_run.main()

os.system('cls')

# 여기서 부터 스크립트 시작!
print(__doc__)


a = int(input("Your Repeatation (1~100,000)? :"))
stack = []

while a >= 1 and a <= pow(10,5):                    # 10**5
    num1 = int(input("Let's stack numbers! :"))

    if (num1 == 0):
        if (len(stack) == 0):
            print('[0]')
        else:
            print(stack[0])
            heapq.heappop(stack)

    elif(num1 >= 1 and num1 < pow(2,31)):
        if num1 in stack:
            a -= 1
            continue
        else:
            heapq.heappush(stack, num1)
    a -= 1

print("Your Stack is .....  ", stack)
