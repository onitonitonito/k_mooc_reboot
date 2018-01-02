"""
# Various Graph in matplotlib.pyplot
# https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-
# a-string-in-python
#
# plt.close() will close the figure window entirely, where plt.clf() will
# just clear the figure - you can still paint another plot onto it.
#
# https://stackoverflow.com/questions/16661790/difference-between-plt-
# close-and-plt-clf
#
#\n\n"""
print(__doc__)

import sys
import numpy as np
import matplotlib.pyplot as plt


def _00():
    # blank_page
    fig = plt.figure(figsize=(7, 5))

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()

    print()


def _01():
    # In[172]:
    plt.clf()
    t = np.arange(10)
    ax = plt.subplot('111')
    ax.plot(t)
    ax.set_xlim((-2, 10))  # plt.xlim((-2,10)) 와 동일
    ax.set_ylim((-2, 10))  # plt.ylim((-2,10)) 와 동일

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _02():
    # In[181]:
    fig = plt.figure(figsize=(7, 5))
    plt.plot(np.arange(10))
    print(fig)  # Figure(700x500)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _03():
    # In[183]:
    t = np.arange(10)

    plt.plot(t)
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _04():
    # In[69]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, 'g.:',)
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _05():
    # In[169]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, 'g.:', lw=5, mew=10)
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _06():
    # In[76]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, 'g.:', lw=5, mew=10)
    plt.xlim((-2, 15))
    plt.ylim((-2, 15))
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _07():
    # In[214]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, 'g.:', lw=5, mew=10)
    plt.xticks(t, 'abcdefghijklmnopqrstuvwxyz')
    plt.yticks(t)
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _08():
    # In[228]:
    plt.clf()          # clear figure
    t = np.arange(10)

    plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _09():
    # In[229]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, t, 'r--', label='lab1')
    plt.plot(t, 0.5 * t**2, 'bs:', label='lab2')
    plt.plot(t, 0.2 * t**3, 'g^-', label='lab3')
    plt.legend(loc=10)
    plt.grid(True)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _10():
    this_func_name = sys._getframe().f_code.co_name
    # In[231]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
    plt.legend(labels=['plot1', 'plot2', 'plot3'], loc='center')
    plt.xlabel("xlabel (x)")
    plt.ylabel("ylabel (y)")
    plt.title("Three Plot : f({:})".format(this_func_name))
    plt.grid(True)

    plt.show()


def _11():
    this_func_name = sys._getframe().f_code.co_name
    # In[251]:
    plt.clf()
    t = np.arange(10)

    plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
    plt.legend(labels=['plot1', 'plot2', 'plot3'], loc='center left')
    plt.xlabel("xlabel (x)")
    plt.ylabel("ylabel (y)")
    plt.title(f"Three Plot : f({this_func_name})")
    plt.annotate(
        'annotate exam',
        xy=(1, 1),
        xytext=(0.5, 30),
        arrowprops=dict(
            facecolor='black',
            shrink=0.05,
            connectionstyle='angle3,angleA=0,angleB=90'
            ),
        )
    plt.gca().invert_yaxis()            # flip y-dir
    plt.gca().invert_xaxis()            # flip x-dir
    plt.grid(True)
    plt.show()


# Axes & subplot

def _12():
    this_func_name = sys._getframe().f_code.co_name
    # In[19]:
    plt.clf()
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    ax1 = plt.subplot(2, 1, 1)  # plt.subplot(211) 동일
    plt.plot(x1, y1, 'ko-')
    plt.title("A tale of 2 subplots : f({:})".format(this_func_name))
    plt.ylabel('Damped oscillation')
    print(ax1)

    ax2 = plt.subplot(2, 1, 2)  # plt.subplot(212) 동일
    plt.plot(x2, y2, 'r.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')
    print(ax2)

    plt.tight_layout()
    plt.show()


def _13():
    this_func_name = sys._getframe().f_code.co_name
    # In[6]:
    plt.clf()
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    ax1.plot(x1, y1, 'ko-')
    ax1.set_title("A tale of 2 subplots : f({:})".format(this_func_name))
    ax1.set_ylabel('Damped oscillation')
    print(ax1)

    ax2.plot(x2, y2, 'r.-')
    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('Undamped')
    print(ax2)

    plt.tight_layout()
    plt.show()


def _14():
    # In[8]:
    plt.clf()
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(
        nrows=2, ncols=2, figsize=(20, 10))
    ax11.plot(x1, y1, 'ko-')
    ax11.set_ylabel('Damped oscillation')
    ax11.set_title('ax11')
    print(ax11)

    ax12.plot(x2, y2, 'r.-')
    ax12.set_xlabel('time (s)')
    ax12.set_ylabel('Undamped')
    ax12.set_title('ax12')
    print(ax12)

    ax21.plot(x1, y1, 'ko-')
    ax21.set_ylabel('Damped oscillation')
    ax21.set_title('ax21')
    print(ax21)

    ax22.plot(x2, y2, 'r.-')
    ax22.set_xlabel('time (s)')
    ax22.set_ylabel('Undamped')
    ax22.set_title('ax22')
    print(ax22)

    plt.tight_layout()

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _15():
    # In[13]:
    plt.clf()
    plt.subplot(2, 2, 1)
    plt.subplot(2, 2, 2)
    plt.subplot(2, 2, 3)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


def _16():
    # In[15]:
    plt.clf()
    plt.subplot(2, 2, (1, 2))
    plt.subplot(2, 2, 3)
    plt.subplot(2, 2, 4)

    this_func_name = sys._getframe().f_code.co_name
    plt.title(this_func_name)
    plt.show()


if __name__ == '__main__':
    # _00()
    # _02()
    # _03()
    # _04()
    # _05()
    # _06()
    # _07()
    # _08()
    # _09()
    # _10()
    _11()
    # _12()
    # _13()
    # _14()
    # _15()
    # _16()
    pass
