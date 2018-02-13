"""
# 예제1 : 1부터 3까지 증가
# 예제2 : 구구단
# 출처: [파이쿵] http://pythonkim.tistory.com/68?category=574914
"""
import tensorflow as tf

def one2three_1():
    """
    state, one = tf.Variable(1), tf.constant(1)
    """
    state = tf.Variable(1)          # mutable = variable
    one = tf.constant(1)          # immutable = constant
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        for _ in range(3):
            state_val, one_val = sess.run([state, one])
            state = tf.add(state, one)  # state + one(constatnt)
            print("state:({}) + one:({}) = stat.add:({})".format(
                state_val,
                one_val,
                state.eval()))
        print()

def one2three_2():
    state = tf.Variable(0)
    one   = tf.constant(1)
    value = tf.add(state, one)
    update = tf.assign(state, value)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for _ in range(3):
            print(sess.run(update))
        print()

def table99_1(which):
    level = tf.constant(which)
    state = tf.Variable(1)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for i in range(1, 10):
            left, right = sess.run(level), sess.run(state)
            state = tf.add(state, 1)

            print('{} x {} = {:2}'.format(left, right, left*right))
        print()

def table99_2(which):
    """ # update를 처리하면 연계된 모든 Tensor 객체도 함께 처리 됨 """
    level  = tf.constant(which)
    state  = tf.Variable(0)
    add    = tf.add(state, 1)
    value  = tf.assign(state, add)
    update = tf.multiply(level, value)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for _ in range(9):
            # left, right, result = sess.run([level, state, update])

            result = sess.run(update)
            left, right = level.eval(), state.eval()

            print('{} x {} = {:2}'.format(left, right, result))
        print()

def table99_3(which):
    left = tf.placeholder(tf.int32)
    right = tf.placeholder(tf.int32)
    update = tf.multiply(left, right)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for i in range(1, 10):
            result = sess.run(update, feed_dict={left: which, right: i})
            print('{} x {} = {:2}'.format(which, i, result))
        print()



if __name__ == '__main__':
    one2three_1()
    # one2three_2()
    #
    # table99_1(7)
    # table99_2(7)
    # table99_3(7)
    pass
