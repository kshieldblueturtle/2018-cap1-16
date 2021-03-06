import tensorflow as tf
import numpy as np
import pickle

from tensorflow_model.settings import *

# for using tensorflow as hyper parameter
INPUT_SIZE = 12288
OUTPUT_SIZE = 2

RESULT = [ False, True ]

def bc_run( feature_vector ) :
    tf.reset_default_graph()
    with tf.device('/gpu:0'):
        x = tf.placeholder(tf.float32, shape=[None, INPUT_SIZE])
        y = tf.placeholder(tf.float32, shape=[None, OUTPUT_SIZE])

        dense_layer_1 = tf.layers.dense(inputs=x, units=4096, activation=tf.nn.relu)
        dense_layer_2 = tf.layers.dense(inputs=dense_layer_1, units=1024, activation=tf.nn.relu)
        dense_layer_3 = tf.layers.dense(inputs=dense_layer_2, units=256, activation=tf.nn.relu)
        dense_layer_4 = tf.layers.dense(inputs=dense_layer_3, units=64, activation=tf.nn.relu)
        dense_layer_5 = tf.layers.dense(inputs=dense_layer_4, units=16, activation=tf.nn.relu)

        y_ = tf.layers.dense(inputs=dense_layer_5, units=OUTPUT_SIZE)
        y_test = tf.nn.softmax(y_)

    # testing session start
    model_saver = tf.train.Saver()
    init = tf.global_variables_initializer()

    tf_config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
    tf_config.gpu_options.allow_growth = True

    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
        sess.run(init)
        model_saver.restore(sess, STATIC_BC_CHECK_POINT)
        output = np.array(sess.run(y_test, feed_dict={x: [feature_vector]})).reshape([-1])
        malware_score = output[-1]
        detected=RESULT[int(output.argmax(-1))]
    return detected, malware_score

def load_data( file_path ) :
    with open(file_path, 'rb') as f :
        return pickle.load(f)

def run( file_path ) :
    feature_vector = load_data(file_path)
    return bc_run(feature_vector)