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

def test3_multi_variable_classification():
    """ Multi Variable Classification = (다중 선택문제)
    # 1개 이상의 스코어(y)를 Softmax()에 넣어서 확률(%)로 변환 시킨다
    # argmax()를 이용하여 1-hot Encoding을 구현한다.
    # 1개의 레이블만 선택한다.
    """
    _a = [n for n in range(1, 10)]    # 9개의 입력값을 준다.
    _a_np = np.array(_a)

    print(_a, type(_a), "\n")         # x = 'list' class
    print(_a_np, type(_a_np), "\n")   # x = 'np.ndarray' class
    print(softmax(_a), "\n")          # make it to (%) probablity

    sum_n = 0                         # 확률의 총 합계=1 (100%)
    for n in softmax(_a):
        sum_n += n
        print("%11.2f %%" %(n*100))
    print(SEP)
    print("SUM : {:}%".format(sum_n*100))


if __name__ == '__main__':
    # test1_ndarray_convert_matrics()
    # test2_like_ones()
    test3_multi_variable_classification()



""" SoftMAx() 산출값 (0~1의 값 ... 전체의 총합=1 )
[  2.12078996e-04   5.76490482e-04   1.56706360e-03   4.25972051e-03
   1.15791209e-02   3.14753138e-02   8.55587737e-02   2.32572860e-01
   6.32198578e-01]

   백분율 확률 환산값 (소프트맥스 값을 백분율로 환산, 9가지 케이스)
       0.02 %
       0.06 %
       0.16 %
       0.43 %
       1.16 %
       3.15 %
       8.56 %
      23.26 %
      63.22 %
____________________
SUM : 100.0%
"""
