import matplotlib.pyplot as plt
import numpy as np

def cos_annotate():
    ax = plt.subplot(111)           # plt.subplot(nrow,ncolumn,nplot) --- (f)
    x = np.arange(0.0, 5.0, 0.01)   # np.range(star, stop, step) --- (v)
    y = np.cos(2*(np.pi)*x)

    plt.ylim(-2,2)
    line, = plt.plot(x, y, lw=2)    # line width = 2
    plt.annotate(
        'Local peak\n(max)', xy=(3, 1), xytext=(3, 1.5),
        arrowprops=dict(facecolor='black', shrink=1),
    )
    plt.show()
#cos_annotate()

def sin_modif():
    Fs = 10         # Fs = Amplitude Scale
    f = 4           # f = frequency

    plt.subplot(211)           # plt.subplot(nrow,ncolumn,nplot) --- (f)
    x = np.arange(0,1,0.01)
    y = np.sin(f*2*np.pi*x)*Fs

    plt.plot(x, y, lw=2)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.grid()

    plt.subplot(212)           # plt.subplot(nrow,ncolumn,nplot) --- (f)
    x1 = np.arange(0, 1.0, 0.01);
    y1 = np.sin(2*np.pi*x)

    plt.plot(x1, y1, lw=1)
    plt.xlabel('radian(pi)')
    plt.ylabel('f(x)')
    plt.grid()

    plt.show()
#sin_modif()

def sincos_at_one():
    x = np.arange(0, 5, 0.001)
    y = (np.sin(2*2*np.pi*x)*0.3-0.8)+0.2*x
    dy = np.cos(2/1.5*np.pi*x)

    plt.figure(figsize=(7,5), facecolor=None, edgecolor=None)
    plt.ylim(-1.2,+1.2)

    plt.plot(x,y, lw=3, label='sin+0.2x')
    plt.plot(x,dy, 'r', label='cos')

    plt.grid()
    plt.legend()
    plt.xlabel('Radian(pi)')
    plt.ylabel('Amplitude')
    plt.title('Example of conbined SIN,COS')

    plt.show()
#sincos_at_one()

def set_parts_labels(title,xlabel,ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend()
    plt.grid()

def multi_subplot():
    plt.figure(figsize=(8,9), facecolor=None, edgecolor=None)
    plt.ylim(-1.2,+1.2)

    x = np.arange(0, 3, 0.001)
    y1 = np.sin(2*np.pi*x)
    y2 = np.cos(2*np.pi*x)
    y3 = (np.sin(2*2*np.pi*x)*0.3-0.8)+0.5*x
    y4 = np.cos(2/1.5*np.pi*x)
    y5 = np.tan(2*np.pi*x)

    plt.subplot(321)        # div_row, div_column, n-th   (2x2-1st.=[1]-2/3-4)
    plt.plot(x,y1, lw=3, label='sin')
    plt.plot(x,y2, 'r', label='cos')
    set_parts_labels('Combined Sin & Cos','Rad(pi)','f(x)',)

    plt.subplot(322)        # div_row, div_column, n-th   (2x2-2nd.=1-[2]/3-4)
    plt.plot(x,y2, 'r', label='cos')
    set_parts_labels('Cos Curve Only','Rad(pi)','',)

    plt.subplot(312)        # div_row, div_column, n-th   (2x1-2nd.=1/[2])
    plt.plot(x,y3, lw=3, label='sin+0.5x')
    plt.plot(x,y4, 'r', label='cos1')
    set_parts_labels('Two Different Sin & Cos','Rad(pi)','f(x)',)

    plt.subplot(313)        # div_row, div_column, n-th   (2x1-2nd.=1/[2])
    plt.ylim(-2,+2)
    plt.xlim(0,+2.5)
    plt.plot(x,y1, lw=2,        label='sin')
    plt.plot(x,y2, 'r', lw=1,   label='cos')
    plt.plot(x,y5, 'p', lw=1,   label='tan')
    set_parts_labels('Sin, Cos & Tan Curve','Rad(pi)','f(x)',)

    plt.show()
multi_subplot()
