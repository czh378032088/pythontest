
import tensorflow as tf
import gym
import time
import numpy as np

env = gym.make('CartPole-v0')

x = tf.placeholder('float',[None,5])
y_ = tf.placeholder('float',[None,1])

w1 = tf.Variable(tf.truncated_normal([5,1000]))
b1 = tf.Variable(tf.truncated_normal([1000]))

w2 = tf.Variable(tf.truncated_normal([1000,1]))
b2 = tf.Variable(tf.truncated_normal([1]))

h1 = tf.sigmoid(tf.matmul(x,w1) + b1)

y = tf.sigmoid(tf.matmul(h1 ,w2) + b2)

loss = tf.reduce_mean(tf.square(y - y_))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

x_temp = []
y_temp = []

i = 0

while(True):
    observation = env.reset()
    temp = [0.0,0.0,0.0,0.0,0.0]
    while True:
        env.render()
        #action = env.action_space.sample()
        '''
        temp[0] = 0.0
        ytest1 = sess.run(y,feed_dict = {x:np.mat(temp)})
        temp[0] = 1.0
        ytest2 = sess.run(y,feed_dict = {x:np.mat(temp)})
        
        


        action = 0
        if ytest1 < ytest2:
            action = 1
        '''
        action = env.action_space.sample()#np.random.randint(0,2)
        observation, reward, done, info = env.step(action)
        #print(type(observation))
        temp = [a for a in observation]
        temp.insert(action,0)
        x_temp.append(temp)
        y_temp.append(reward)

        i = i + 1

        if i == 100:
            print(y_temp)
            print(action)
            #print(ytest1,ytest2)
            
            #print(sess.run(b1))
            for j in range(100):
                sess.run(train_step,feed_dict = {x:np.mat(x_temp),y_:np.mat(y_temp).T})
            print(sess.run(loss,feed_dict = {x:np.mat(x_temp),y_:np.mat(y_temp).T}))
            x_temp.clear()
            y_temp.clear()
            i = 0


        if done:
            break

        '''
        observation, reward, done, info = env.step(action)
        
        print(action)
        print(observation)
        print(reward)
        print(done)
        print(info)
        
        '''
       