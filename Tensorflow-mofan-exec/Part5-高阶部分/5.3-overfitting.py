# 过拟合
# 解决过拟合的两种方法：
#
# 增加训练数据
# 正规化： ①L1 ②L2 ③dropout
# 5.3 Dropout解决Overfitting
# 第一步：加载数据
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3)

# 第二步：定义add_layer()函数
def add_layer(inputs, in_size, out_size, layer_name,
              activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
#   使用dropout进行。keep_prob代表多少比例的数据不被丢弃
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
    if activation_function is None:
        out_puts = Wx_plus_b
    else:
        out_puts = activation_function(Wx_plus_b)
    tf.summary.histogram(layer_name+'/outputs', out_puts)
    return out_puts

# 第三步：为网络输入定义palceholder
keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32, [None, 64])#8*8
ys = tf.placeholder(tf.float32, [None, 10])

# 第四步：构建网络
# 定义隐藏层和输出层
l1 = add_layer(xs, 64, 50, 'l1', activation_function=tf.nn.tanh)
prediction = add_layer(l1, 50, 10, 'l2', activation_function=tf.nn.softmax)
# 定义损失函数，并将损失值进行图表显示
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
tf.summary.scalar('loss', cross_entropy)
# 训练
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# 第五步：summary进行合并
sess = tf.Session()
merged = tf.summary.merge_all()

# train图表保存和test图表保存
train_writer = tf.summary.FileWriter('logs/train', sess.graph)
test_writer = tf.summary.FileWriter('logs/test', sess.graph)

# 第六步：变量初始化和激活
init = tf.global_variables_initializer()
sess.run(init)

# 第七步：进行训练1000次
for i in range(1000):
    sess.run(train_step, feed_dict={xs:X_train, ys:y_train, keep_prob: 0.5})
    if i % 50 ==0:
        # recode loss
        train_result = sess.run(merged, feed_dict={xs: X_train, ys: y_train, keep_prob: 1})
        test_result = sess.run(merged, feed_dict={xs: X_test, ys: y_test, keep_prob: 1})
        train_writer.add_summary(train_result, i)
        test_writer.add_summary(test_result, i)

# tensorboard --logdir logs
