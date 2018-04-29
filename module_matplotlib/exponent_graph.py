import numpy as np
import matplotlib.pyplot as plt

# 그래프 파마래터 딕셔녀리 - 선택가능. = 라인스타일은 4종류 다
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

PARA_DICT = [
        {'lw': 1, 'ls': ':',  'color':'#ff9999', 'label': '1st.'},
        {'lw': 1, 'ls': '--', 'color':'#9999ff', 'label': '2nd.'},
        {'lw': 1, 'ls': '-.',  'color':'#e13447', 'label': '3rd.'},
        {'lw': 1, 'ls': '-', 'color':'#6e7397', 'label': '4th'},
        {'lw': 1, 'ls': ':', 'color':'#882277', 'label': '5th'},
        {'lw': 1, 'ls': '-.', 'color':'#113399', 'label': '6th'},
    ]

""" 1. 그래프를 그리는 옵션 """
# x축의 해상도를 설정한다 (시작, 끝, div_number)
x_spacing = (-10, +50, 300)        # x 그래프의 범위
x = np.linspace(*x_spacing)

y1 = 1.03 ** x
y2 = -1.05 ** x
y3 = -1.08 ** -x
y4 = 1.1 ** -x
y5 = np.log(x)
y6 = np.exp(x)

plt.plot(x, y1, **PARA_DICT[0])
plt.plot(x, y2, **PARA_DICT[1])
plt.plot(x, y3, **PARA_DICT[2])
plt.plot(x, y4, **PARA_DICT[3])
plt.plot(x, y5, **PARA_DICT[4])
plt.plot(x, y6, **PARA_DICT[5])

print("x", x)

""" 2. 그래프에 텍스트를 입히는 옵션 """
plt.legend()
# plt.title("Simple Plot")        # 타이틀
# plt.xlabel('x label')           # x 라벨
# plt.ylabel('y label')           # y 라벨

""" 3. 기타 라인/제한 옵션 """
plt.grid(b=None, which='major', axis='both')
# plt.xlim(-10, x_spacing[1])
plt.xlim(-10, 10)
plt.ylim(-3, 3 )

""" 4. 그리기 """
plt.show()
