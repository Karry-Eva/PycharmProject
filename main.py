import os
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"    # 消除运行警告

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
sess = tf.Session()#tensorflow1.0使用，2.0不再使用，需要忽略2.0
print(sess.run(result))
