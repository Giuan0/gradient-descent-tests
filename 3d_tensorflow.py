import tensorflow as tf
import numpy as np

# lr = 0.1 
x = tf.Variable(38.0, tf.float32)
y = tf.Variable(-18.0, tf.float32)

function = tf.square(x) - tf.square(y)

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(function)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

print(sess.run(x), '-', sess.run(y))
sess.run(train)
print(sess.run(x), '-', sess.run(y))
