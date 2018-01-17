""" Create a constant op
# This op is added as a node to the default graph
"""
import tensorflow as tf

def tf_hello_world():
    hello = tf.constant("Hello, Tensorflow World!")

    """ sort a TF session """
    sess = tf.Session()

    """ run the op and get result
    # sess.run(hello) = <class 'type'> : bytes literals.
    # byte.decode('utf-8') = String
    """
    print(sess.run(hello).decode("utf-8"))
# tf_hello_world()

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)                # tf.float32 automatically added.
node3 = tf.add(node1, node2)

print("node1= ", node1)
print("node2= ", node2)
print("node3= ", node3, end="\n\n")

sess = tf.Session()
# 2018-01-23 20:43:12.619723: I C:\tf_jenkins\home\workspace\rel-win.....

print("sess.run([node1, node2])= ", sess.run([node1, node2]))
print("sess.run(node3)= ", sess.run(node3))
