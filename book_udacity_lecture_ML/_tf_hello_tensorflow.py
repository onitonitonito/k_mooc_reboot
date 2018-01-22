""" Create a constant op
# This op is added as a node to the default graph
"""
import tensorflow as tf

def tf_hello_world():
    """ run the op and get result
    # sess.run(hello) = <class 'type'> : bytes literals.
    # byte.decode('utf-8') = String
    """
    hello = tf.constant("Hello, Tensorflow World!")

    """ sort a TF session """
    sess = tf.Session()

    print(sess.run(hello).decode("utf-8"))

def tf_calculation_add():
    node1 = tf.constant(3.0, tf.float32)
    node2 = tf.constant(4.0)                # tf.float32 automatically added.
    node3 = tf.constant(1.0)                # tf.float32 automatically added.
    result = tf.add(node1, node2)

    print("node1 = ", node1)    # constant:[1x1]
    print("node2 = ", node2)    # constant:[2x1]
    print("node3 = ", node3)    # constant:[3x1].. vari added in const_matrics
    print("result= ", result, end="\n\n")   # result added in add_matrics

    sess = tf.Session()
    # 2018-01-23 20:43:12.619723: I C:\tf_jenkins\home\workspace\rel-win.....

    print()
    print("sess.run([node1, node2])= ", sess.run([node1, node2]))
    print("sess.run(result)= ", sess.run(result))



if __name__ == '__main__':
    # tf_hello_world()
    tf_calculation_add()
