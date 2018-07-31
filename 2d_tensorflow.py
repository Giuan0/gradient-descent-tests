import tensorflow as tf
import numpy as np

# lr = 0.1 
x = tf.Variable(-9.0, tf.float32)

function = tf.square(x)

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(function)

sess = tf.Session()
sess.run(tf.initialize_all_variables())
sess.run(train)

print(sess.run(x))
