import tensorflow as tf

hello = tf.constant('Hello,TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(3)
b = tf.constant(4)
with tf.Session() as sess:
    print(sess.run(a + b))
    print(sess.run(a * b))
    print(sess.run(a / b))
    print(sess.run(a ** b))

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a , b)
mul = tf.multiply(a , b)

with tf.Session() as sess:
    print(sess.run(add,feed_dict={a:3,b:5}))
    print(sess.run(mul,feed_dict={a:3,b:5}))

matrix1 = tf.constant([[3.,3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1,matrix2)

with tf.Session() as sess:
    print(sess.run(product))
    print(sess.run(tf.matmul(matrix2,matrix1)))
