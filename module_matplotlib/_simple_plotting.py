""" 넘파이 수식연산 및 맷플롯리브 연습1
# 파이플롯 명령어 찾기 :
# https://matplotlib.org/api/pyplot_api.html
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def test_show_linestyle():
    color = 'cornflowerblue'
    points = np.ones(5)  # Draw 5 points for each line
    text_style = dict(horizontalalignment='right', verticalalignment='center',
                      fontsize=12, fontdict={'family': 'monospace'})

    def format_axes(ax):
        ax.margins(0.2)
        ax.set_axis_off()

    def nice_repr(text):
        return repr(text).lstrip('u')

    # Plot all line styles.
    fig, ax = plt.subplots()
    linestyles = ['-', '--', '-.', ':']

    for y, linestyle in enumerate(linestyles):
        ax.text(-0.1, y, nice_repr(linestyle), **text_style)
        ax.plot(y * points, linestyle=linestyle, color=color, linewidth=3)
        format_axes(ax)
        ax.set_title('The Line Styles')

    plt.show()
test_show_linestyle()       # Show 4-line styles in legend


def test_simple_plot():
    # x = list(range(0, 81, 1))     # 일반 list를 쓰지 못함.
    x = np.arange(0, 81, 1)
    print(x)

    args = [
        {'lw': 5, 'ls': ':', 'color': '#ff9999', 'label': 'first'},
        {'lw': 10, 'ls': '--', 'color': '#9999ff', 'label': 'second'},
        {'lw': 3, 'ls': '-.', 'color': '#ee3377', 'label': 'third'}, ]

    plt.plot(x, np.sqrt(x), **args[0])
    plt.plot(x, 3e-3 * x**2,  **args[1])
    plt.plot(x, 1.45e-1 * x,  **args[2])
    # plt.plot(x, np.sqrt(x), args[0])
    # plt.plot(x, 3e-3*x**2,  args[1])
    # plt.plot(x, 1.45e-1*x,  args[2])

    plt.axis([0, 81, 0, 10])   # [x=0~81, y=0,10]
    plt.grid()
    plt.legend()
    plt.show()
test_simple_plot()          # So simple examples

def line_plot_random():
    y = [.1, .5, 1.2, 1.3, 2.1, 2.5, 2.7, 2.9, 3.5, 3.7, 4.7, 5.1, 6.1]
    plt.plot(y, lw=5)
    plt.ylabel('y-axis numbers')
    plt.xlabel('x-axis numbers')
    plt.grid()
    plt.show()

def line_graph():
    """ '맷플롯리브'의 기본적인 그리기와 설정변경
    # 예제 : 싸인함수 그리기 : http://pinkwink.kr/967
    """
    x = np.linspace(0, 1, 50)
    print("x", x)

    plt.plot(x, -1 * np.log(x), label='logarithm_minus, y=0 ... infinie')
    plt.plot(x, -1 * np.log(1 - x), label='logarithm_plus,    y=1 ... infinie')
    # plt.plot(x, 1/(1+np.exp(-x)**2), label='linear')
    # plt.plot(x, np.sqrt(x), label='linear')
    # plt.plot(x, x, label='linear')
    # plt.plot(x, x**2, label='quadratic')
    # plt.plot(x, x**3, label='cubic')
    # plt.plot(x, x**4, label='custom.1')
    # plt.plot(x, x**5, label='custom.2')

    plt.title("Simple Plot")
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.legend()

    plt.grid(b=None, which='major', axis='both')
    plt.ylim(0, 6)
    plt.xlim(0, 1)
    plt.show()

def tangential_graph():
    pass

def bar_chart_with_value():
    n = 12                      # number of bar
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.figure(figsize=(7, 5))           # window size

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='grey')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='grey')

    for x, y in zip(X, Y1):
        plt.text(x, y + 0.03, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, Y2):
        plt.text(x, -y - 0.03, '%.2f' % y, ha='center', va='top')

    plt.xlim(-.5, n), plt.xticks([])
    plt.ylim(-1.25, +1.25), plt.yticks([])
    plt.show()

def text_equation_cloud():
    eqs = []
    eqs.append(
        (r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
    eqs.append(
        (r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
    eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
    eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
    eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

    plt.figure(figsize=(7, 5))

    for i in range(24):
        index = np.random.randint(0, len(eqs))
        eq = eqs[index]
        size = np.random.uniform(12, 32)
        x, y = np.random.uniform(0, 1, 2)
        alpha = np.random.uniform(0.25, .75)
        plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
                 transform=plt.gca().transAxes, fontsize=size, clip_on=True)

    plt.xticks([]), plt.yticks([])
    plt.show()

def matplot_test01():
    """
    # Created on Sun Jan  7 13:21:40 2018
    # @author: nitt0
    """
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t):
        """
        # (1) y(t) = e(-t) * cos(2*pi*t)   ... [2][1]열의 [1]번째 배치
        # (2) y(t) = cos(2 * pi * t)       ... [2][1]열의 [2]번째 배치
        """
        return np.exp(-t) * np.cos(2 * np.pi * t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    plt.show()

def matplot_test02():
    """
    Created on Sun Jan  7 13:21:40 2018
    @author: nitt0
    """
    import numpy as np
    import matplotlib.pyplot as plt

    def value(x_value):
        return x_value**2

    x_range = np.arange(1, 20, 0.5)

    plt.figure(1)
    plt.plot(x_range, value(x_range), 'r--')
    #plt.plot(x_range, value(x_range), 'r--')
    plt.show()


if __name__ == '__main__':
    # matplot_test01()
    # matplot_test02()
    # line_graph()
    # line_plot_random()
    # tangential_graph()
    # matplot_test01()
    # matplot_test02()
    # bar_chart_with_value()
    text_equation_cloud()
    pass
