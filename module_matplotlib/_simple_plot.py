import numpy as np
import matplotlib.pyplot as plt

# 그래프 파마래터 딕셔녀리 - 선택가능.
PARA_DICT = [
    {'lw': 3, 'ls': ':', 'color': '#ff9999', 'label': 'first'},
    {'lw': 5, 'ls': '--', 'color': '#9999ff', 'label': 'second'},
    {'lw': 3, 'ls': '-.', 'color': '#ee3377', 'label': 'third'}, ]


def simple_line_graph():
    x_args = [0, 50, 50]

    """ 1. 그래프를 그리는 옵션 """
    # x축의 해상도를 설정한다 (시작, 끝, div_number)
    x = np.linspace(*x_args)
    y1 = (1 + 1/x)**x
    y2 = 1e-3*x**2 + 1

    plt.plot(x, y1, **PARA_DICT[0])
    plt.plot(x, y2, **PARA_DICT[1])
    plt.legend()
    print("x", x)

    """ 2. 그래프에 텍스트를 입히는 옵션 """
    plt.title("Simple Plot")        # 타이틀
    plt.xlabel('x label')           # x 라벨
    plt.ylabel('y label')           # y 라벨

    """ 3. 기타 라인/제한 옵션 """
    plt.grid(b=None, which='major', axis='both')
    plt.ylim(1, 2.75)
    plt.xlim(0, x_args[1])

    """ 4. 그리기 """
    plt.show()

simple_line_graph()
