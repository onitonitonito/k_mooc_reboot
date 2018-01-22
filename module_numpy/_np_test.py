""" 넘파이 문제에 대한 테스트 페이지
# reshape((r,c)) = r x c 행렬로 만들어 줌
# ones_like(a) = 값이 1인 행렬반환
"""
import numpy as np
import matplotlib.pyplot as plt
SEP = "__"*10

def test1_ndarray_convert_matrics():
    """ 넘파이 a레인지 / 넘파이 행렬 = <넘파이 ndarray 클래스>
    # reshape() : 행렬로 바꾸는 함수 = ndarray.reshape()
    """
    x = np.arange(start=0, stop=6, step=1)      # 간단히, np.arange(6)
    x1 = x.reshape((2,3))                       # [2x3] 행렬로 제정렬
    print(SEP, "\nnp.arange = %s\n%s\n" %(x, type(x)))
    print(SEP, "\nnp.ndarray.reshape(2,3) = \n%s\n%s" %(x1, type(x1)))

def test2_like_ones():
    """ 넘파이. 원즈_라잌(a)
    # a와 같은 dtype으로 같은갯수의 1의 배열(ndarray)을 반환한다
    # if dtype=float .. [1., 1., 1., 1., 1.]
    """
    x = np.arange(6, dtype=np.float)    #.. np.float(x) = return 'float'
    x1 = x.reshape((2, 3))
    x2 = np.ones_like(x1)
    print(SEP, "\nnp.arange = %s\n%s\n" %(x, type(x)))
    print(SEP, "\nnp.arange = \n%s\n%s\n" %(x1, type(x1)))
    print(SEP, "\nnp.ndarray.reshape(2,3) = \n%s\n%s" %(x2, type(x2)))

def softmax(x):
    """ Compute softmax values for each sets of SCORES in x.
    # 소프트맥스() = x 값(스코어)을 받아 확률로 변환 해 줌.
    # x 값을 단일 int값으로 받으면 확율 1.0만 반환한다.
    # x 값은 Array로 입력 - 다중후보가 필요하다.= np.ndarray 클래스
    """
    # TODO: Compute and return softmax(x)
    return np.exp(x) / np.sum(np.exp(x), axis=0)


if __name__ == '__main__':
    # test1_ndarray_convert_matrics()
    # test2_like_ones()
    _a = [n for n in range(1, 10)]
    _a_np = np.array(_a)

    print(_a, type(_a))         # x = 'list' class
    print(_a_np, type(_a_np))   # x = 'np.ndarray' class
    print(softmax(_a))          # make it to probablity
