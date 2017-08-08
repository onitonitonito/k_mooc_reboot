import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def line_plot_simple():
    y = [.1,.5,1.2,1.3,2.1,2.5,2.7,2.9,3.5,3.7,4.7,5.1,6.1]
    plt.plot(y, lw=5)
    plt.ylabel('y-axis numbers')
    plt.xlabel('x-axis numbers')
    plt.grid()
    plt.show()
#line_plot_simple()

def bar_chart_with_value():
    n = 12                      # number of bar
    X = np.arange(n)
    Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
    Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

    plt.figure(figsize=(7,5))           # window size

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='grey')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='grey')

    for x,y in zip(X,Y1):
        plt.text(x, y+0.03, '%.2f'%y, ha='center', va= 'bottom')

    for x,y in zip(X,Y2):
        plt.text(x, -y-0.03, '%.2f'%y, ha='center', va= 'top')

    plt.xlim(-.5,n), plt.xticks([])
    plt.ylim(-1.25,+1.25), plt.yticks([])
    plt.show()
#bar_chart_with_value()

def text_equation_cloud():
    eqs = []
    eqs.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
    eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
    eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
    eqs.append((r"$E = mc^2 = \sqrt{{m_0}^2c^4 + p^2c^2}$"))
    eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

    plt.figure(figsize=(7,5))

    for i in range(24):
        index = np.random.randint(0,len(eqs))
        eq = eqs[index]
        size = np.random.uniform(12,32)
        x,y = np.random.uniform(0,1,2)
        alpha = np.random.uniform(0.25,.75)
        plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
                 transform=plt.gca().transAxes, fontsize=size, clip_on=True)

    plt.xticks([]), plt.yticks([])
    plt.show()
text_equation_cloud()
