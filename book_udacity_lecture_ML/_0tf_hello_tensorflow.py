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
        print(sess.run(hello))      # return = b'Hello Tensorflow World!!'
        print(sess.run(hello).decode("utf-8"))

def tf_calculation_add(n1_val, n2_val, n3_val):
    """ n1_val, n2_val, n3_val = float32 value """
    node1 = tf.constant(
        value=n1_val, dtype=tf.float32,
        shape=[1], name="Const", verify_shape=False )
    node2 = tf.constant(value=n2_val)           # tf.float32 automatically added.
    node3 = tf.Variable(initial_value=n3_val)   # tf.trainable variables
    result = tf.add(node1, node2)
    return node1, node2, node3, result


if __name__ == '__main__':
    # tf_hello_world()

    node1, node2, node3, result = tf_calculation_add(3., 4., 1.)
    print("node1 = {:}\nnode2 = {:}\nnode3 = {:}\n".format(
        node1,     # Tensor("Const:0", shape=(1,), dtype=float32)
        node2,     # Tensor("Const_1:0", shape=(), dtype=float32)
        node3))    # <tf.Variable 'Variable:0' shape=() dtype=float32_ref>
    print("result= ", result, end="\n\n")   # result added in add_matrics

    # 2018-01-23 20:43:12.619723: I C:\tf_jenkins\home\workspace\rel-win.....
    with tf.Session() as sess:
        print()
        print("sess.run([node1, node2])= {:}\nsess.run(result)= {:}".format(
            sess.run([node1, node2]),
            sess.run(result)))
