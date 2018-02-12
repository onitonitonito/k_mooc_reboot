""" TOLKIEN's Example for Voice Recogniton (M or F?)
# Training Data : voice.csv
# Lab 5 Logistic Regression Classifier
# reference : https://www.kaggle.com/primaryobjects/voicegender
"""
import os
import numpy as np
import urllib.request
import tensorflow as tf

CSV_DIR = os.path.join(os.path.dirname(__file__), '_csv_hunkim\\')

r = urllib.request.urlopen(
    'https://raw.githubusercontent.com/primaryobjects/voice-gender/master/voice.csv')
r.readline()                    # r 객체에서 한 줄 팝 아웃 (readline)
voice_csv = r.read()            # r 객체에서 잔여라인을 뽑아옴(read)

with open(CSV_DIR+'voice.csv', 'wb') as f:
    f.write(voice_csv)

tf.set_random_seed(743)  # for reproducibility
file_queue = tf.train.string_input_producer(
    [CSV_DIR+'voice.csv'], name='file_queue')

reader = tf.TextLineReader()
_, value = reader.read(file_queue)

conv_dic = { b'male': 1., b'female' : 0.}
record_defaults = [
    [0.], [0.], [0.], [0.], [0.],
    [0.], [0.], [0.], [0.], [0.],
    [0.], [0.], [0.], [0.], [0.],
    [0.], [0.], [0.], [0.], [0.], [b'male']]

xy = tf.decode_csv(value, record_defaults=record_defaults)

# collect batches of csv in
train_x_batch, train_y_batch = tf.train.batch(
    [xy[2:6], xy[-1:]],
    batch_size=32)

# build a model
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(tf.matmul(X, W)))
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# train a model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    x_data, y_data = sess.run([train_x_batch, train_y_batch])

    for step in range(4001):
        x_data, y_data = sess.run([train_x_batch, train_y_batch])
        for i in range(32):
            y_data[i][0] = conv_dic[y_data[i][0]]
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print("{:5}. __ cost= {:}".format(step, cost_val))

    for step in range(11):
        # accuracy report
        x_data, y_data = sess.run([train_x_batch, train_y_batch])

        for i in range(32):
            y_data[i][0] = conv_dic[y_data[i][0]]

        hypo_val, cost_val, accu_val = sess.run(
            [hypothesis, predicted, accuracy],
            feed_dict={X: x_data, Y: y_data})

        if step % 1 == 0:
            print("Accuracy: ", accu_val)

    coord.request_stop()
    coord.join(threads)
