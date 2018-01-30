"""
텐서플로우 명령어 이해하기
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# sess = tf.Session()

def show_shape(tf_constant_matrics):
    print(tf.shape(tf_constant_matrics))

def shape_rank_axis():
    """ Shape(행렬) / Rank(차원) / Axis(대각주): Axis=0,1,2,3
    # Tensor("Shape:0", shape=(4,), dtype=int32)
    # Tensor("Shape_1:0", shape=(3,), dtype=int32)
    # Tensor("Shape_2:0", shape=(2,), dtype=int32)
    # Tensor("Shape_3:0", shape=(1,), dtype=int32)
    """
    t1 = tf.constant([1,2,3,4])
    t3 = tf.constant([[[1,2,3],[3,4,5]]])
    t2 = tf.constant([[1,2],[3,4]])
    t4 = tf.constant([[[[1,2,3,4],[5,6,7,8],[9,0,1,0]],
        [[4,3,2,1],[9,8,7,6],[5,4,3,2]]]])

    show_shape(t1)
    show_shape(t2)
    show_shape(t3)
    show_shape(t4)

    print()
    print(t1)
    print(t2)
    print(t3)
    print(t4)
shape_rank_axis()

_a = tf.constant([[1.,2.],[3.,4.]])
_b = tf.constant([[3.,6.],[9.,2.]])
_c = tf.matmul(_a, _b)
print(_a)
print(_b)
print("\n_c = ",_c)

print(tf.reduce_mean(_a, axis=0))
print(tf.reduce_mean(_a, axis=1))
