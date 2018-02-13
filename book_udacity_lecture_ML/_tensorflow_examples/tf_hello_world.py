""" Create a constant op
# This op is added as a node to the default graph
"""
import tensorflow as tf

def tf_hello_world():
    """ run the op and get result
    # sess.run(hello) = <class 'type'> : bytes literals.
    # byte.decode('utf-8') = String
    """
    hello = tf.constant("Hello Tensorflow World!!")

    """ sort a TF session """
    with tf.Session() as sess:
        print()
        print(sess.run(hello))      # return = b'Hello Tensorflow World!!'
        print(sess.run(hello).decode("utf-8"))

a = tf.constant([[1, 2]])     # (1,2)
b = tf.constant([[2],[3]])  # (2,1)
c = tf.add(a, b)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # writer = tf.summary.FileWriter('../_logdir', sess.graph)
    c_val = sess.run(c)
    print(c_val)

if __name__ == '__main__':
    # tf_hello_world()
    pass
