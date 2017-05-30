import matplotlib.tri as mtri
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def tri_tri():
    x = np.asarray([0, 1, 2, 3, 4, 2])
    y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
    triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
    triang = mtri.Triangulation(x, y, triangles)
    plt.triplot(triang, 'ko-')
    plt.xlim(-0.1, 4.1)
    plt.ylim(-0.1, 3.7)
    plt.show()
#tri_tri()

def tri_multi():
    x = np.asarray([0, 1, 2, 3, 4, 2])
    y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
    triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
    triang = mtri.Triangulation(x, y, triangles)

    refiner = mtri.UniformTriRefiner(triang)
    triang2 = refiner.refine_triangulation(subdiv=2)

    plt.triplot(triang2, 'ko-')
    plt.xlim(-0.1, 4.1)
    plt.ylim(-0.1, 3.7)
    # plt.show()
# tri_multi()

def tri_2Dcolor_contour():
    x = np.asarray([0, 1, 2, 3, 4, 2])
    y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
    triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
    triang = mtri.Triangulation(x, y, triangles)

    refiner = mtri.UniformTriRefiner(triang)
    triang2 = refiner.refine_triangulation(subdiv=2)

    triang5 = refiner.refine_triangulation(subdiv=5)
    z5 = np.cos(1.5*triang5.x)*np.cos(1.5*triang5.y)

    plt.triplot(triang2, 'ko-')
    plt.xlim(-0.1, 4.1)
    plt.ylim(-0.1, 3.7)

    plt.tricontourf(triang5, z5)
    plt.show()
#tri_2Dcolor_contour()

def tri_3Dcolor_contour_all():
    fig = plt.figure(figsize=(8,6))

    x = np.asarray([0, 1, 2, 3, 4, 2])
    y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
    triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
    triang = mtri.Triangulation(x, y, triangles)

    refiner = mtri.UniformTriRefiner(triang)
    triang2 = refiner.refine_triangulation(subdiv=2)

    triang3 = refiner.refine_triangulation(subdiv=3)
    z3 = np.cos(1.5 * triang3.x) * np.cos(1.5 * triang3.y)

    triang5 = refiner.refine_triangulation(subdiv=5)
    z5 = np.cos(1.5*triang5.x)*np.cos(1.5*triang5.y)

    ax = fig.gca(projection='3d')

    plt.xlim(-0.1, 4.1)
    plt.ylim(-0.1, 3.7)
    plt.triplot(triang2, 'ko-')
    plt.tricontourf(triang5, z5)

    ax.plot_trisurf(triang3.x, triang3.y, z3, cmap=cm.jet, linewidth=0.2)
    ax.tricontourf(triang3, z3, zdir='z', offset=-1.2, cmap=cm.coolwarm)
    ax.set_zlim(-1, 1)
    ax.view_init(40, -40)

    '''
    refer.MD = [Data Science School](https://goo.gl/ILPdUh)
    refer QnA = http://stackoverflow.com/questions/14415741/numpy-array-vs-asarray
    '''
#tri_3Dcolor_contour_all()

def plot_3Dcontour_surfer():
    fig = plt.figure(figsize=(7,6))

    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(-2,2)

    '''
    Refer: http://pinkwink.kr/976 [PinkWink]
    '''


tri_3Dcolor_contour_all()
plot_3Dcontour_surfer()
plt.show()
