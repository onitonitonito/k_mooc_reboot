import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D


def scatter_chart():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()


def bar_chart():
    n_groups = 5

    means_men = (20, 35, 30, 35, 27)
    std_men = (2, 3, 4, 1, 2)

    means_women = (25, 32, 34, 20, 25)
    std_women = (3, 5, 2, 3, 3)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, color='b',
                    yerr=std_men, error_kw=error_config,
                    label='Men')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                    alpha=opacity, color='r',
                    yerr=std_women, error_kw=error_config,
                    label='Women')

    ax.set_xlabel('Group')
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
    ax.legend()

    fig.tight_layout()
    plt.show()


def boxed_chart():
    fig, ax = plt.subplots()
    ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                   facecolors=('red', 'yellow', 'green'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('seconds since start')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Bill', 'Jim'])
    ax.grid(True)
    ax.annotate('race interrupted', (61, 25),
                xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=16,
                horizontalalignment='right', verticalalignment='top')

    plt.show()


def pie_chart():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    plt.show()


def histo_chart():
    np.random.seed(19680801)

    n_bins = 10
    x = np.random.randn(1000, 3)

    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax0, ax1, ax2, ax3 = axes.flatten()

    colors = ['red', 'tan', 'lime']
    ax0.hist(x, n_bins, density=True, histtype='bar',
             color=colors, label=colors)
    ax0.legend(prop={'size': 10})
    ax0.set_title('bars with legend')

    ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
    ax1.set_title('stacked bar')

    ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
    ax2.set_title('stack step (unfilled)')

    # Make a multiple-histogram of data-sets with different length.
    x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
    ax3.hist(x_multi, n_bins, histtype='bar')
    ax3.set_title('different sample sizes')

    fig.tight_layout()
    plt.show()


def boxplot_chart():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)

    fig, axs = plt.subplots(2, 3)

    # basic plot
    axs[0, 0].boxplot(data)
    axs[0, 0].set_title('basic plot')

    # notched plot
    axs[0, 1].boxplot(data, 1)
    axs[0, 1].set_title('notched plot')

    # change outlier point symbols
    axs[0, 2].boxplot(data, 0, 'gD')
    axs[0, 2].set_title('change outlier\npoint symbols')

    # don't show outlier points
    axs[1, 0].boxplot(data, 0, '')
    axs[1, 0].set_title("don't show\noutlier points")

    # horizontal boxes
    axs[1, 1].boxplot(data, 0, 'rs', 0)
    axs[1, 1].set_title('horizontal boxes')

    # change whisker length
    axs[1, 2].boxplot(data, 0, 'rs', 0, 0.75)
    axs[1, 2].set_title('change whisker length')

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.4, wspace=0.3)

    # fake up some more data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 40
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
    data.shape = (-1, 1)
    d2.shape = (-1, 1)
    # Making a 2-D array only works if all the columns are the
    # same length.  If they are not, then use a list instead.
    # This is actually more efficient because boxplot converts
    # a 2-D array into a list of vectors internally anyway.
    data = [data, d2, d2[::2, 0]]

    # Multiple box plots on one Axes
    fig, ax = plt.subplots()
    ax.boxplot(data)

    plt.show()


def color_box_chart():
    # Random test data
    np.random.seed(19680801)
    all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

    # rectangular box plot
    bplot1 = axes[0].boxplot(all_data,
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=labels)  # will be used to label x-ticks
    axes[0].set_title('Rectangular box plot')

    # notch shape box plot
    bplot2 = axes[1].boxplot(all_data,
                             notch=True,  # notch shape
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=labels)  # will be used to label x-ticks
    axes[1].set_title('Notched box plot')

    # fill with colors
    colors = ['pink', 'lightblue', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    # adding horizontal grid lines
    for ax in axes:
        ax.yaxis.grid(True)
        ax.set_xlabel('Three separate samples')
        ax.set_ylabel('Observed values')

    plt.show()


def iso_3d_chart():
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    ax1 = plt.subplot(2, 1, 1, projection='3d')
    plt.plot(x1, y1, 'ko-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')
    print(ax1)

    ax2 = plt.subplot(2, 1, 2, projection='3d')
    plt.plot(x2, y2, 'r.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')
    print(ax2)

    plt.tight_layout()
    plt.show()


def spiral():
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    z = np.linspace(0, 1, 100)
    x = z * np.sin(20 * z)
    y = z * np.cos(20 * z)

    c = x + y

    ax.scatter(x, y, z, c=c)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot(x, y, z, '-b')
    plt.show()


def hat_chart():
    x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
    y = x.copy().T
    z = np.cos(x ** 2 + y ** 2)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(x, y, z, cmap=plt.cm.jet,
                    rstride=1, cstride=1, linewidth=0)

    plt.show()


def spear_chart():
    u = np.linspace(0, np.pi, 30)
    v = np.linspace(0, 2 * np.pi, 30)

    x = np.outer(np.sin(u), np.sin(v))
    y = np.outer(np.sin(u), np.cos(v))
    z = np.outer(np.cos(u), np.ones_like(v))


    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_wireframe(x, y, z)
    plt.show()


if __name__ == '__main__':
    # scatter_chart()
    # bar_chart()
    # boxed_chart()
    # pie_chart()
    # histo_chart()
    # boxplot_chart()
    # color_box_chart()
    # iso_3d_chart()
    # spiral()
    # hat_chart()
    spear_chart()
    pass
