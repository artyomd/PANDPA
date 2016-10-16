__author__ = 'artyomd'
import numpy as np
def perceptron(x, y, theta):
    for j in range (0,400):
        for i in range(0,len(x)):
            mistake = y[i]*np.dot(theta,x[i])
            if mistake<=0:
                theta = theta + y[i]*x[i]
    return theta
def averagePerceptron(x,y,theta):
    thetas = []
    thetas.append(theta)
    for j in range(0,400):
        for i in range(0,len(x)):
            mistake = y[i]*np.dot(theta,x[i])
            if mistake<=0:
                theta = theta + y[i]*x[i]
                thetas.append(theta)
    averagedTheata=[0]*len(theta)
    averagedTheata=np.array(averagedTheata)
    averagedTheata=np.array(averagedTheata, dtype='f')
    for i in range(0,len(thetas)):
        averagedTheata+=thetas[i]
    averagedTheata/=(len(thetas))
    return averagedTheata
def PA(x,y,theta):
    lambda_=10
    for j in range (0,400):
        for i in range(0,len(x)):
            mistake = y[i]*np.dot(theta,x[i])
            if mistake<=0:
                xm=sumsq(x[i])
                LH = 1-mistake
                xeta = min(float(LH)/float(xm),float(1)/float(lambda_))
                theta = theta + xeta*y[i]*x[i]
    return theta
def APA(x,y,theta):
    thetas = []
    thetas.append(theta)
    lambda_=0.10
    for j in range(0,400):
        for i in range(0,len(x)):
            mistake = y[i]*np.dot(theta,x[i])
            if mistake<=0:
                xm=sumsq(x[i])
                LH = 1-mistake
                xeta = min(float(LH)/float(xm),float(1)/float(lambda_))
                theta = theta + xeta*y[i]*x[i]
                thetas.append(theta)
    averagedTheata=[0]*len(theta)
    averagedTheata=np.array(averagedTheata)
    averagedTheata=np.array(averagedTheata, dtype='f')
    for i in range(0,len(thetas)):
        averagedTheata+=thetas[i]
    averagedTheata/=(len(thetas))
    return averagedTheata
def sumsq(a):
    sum = 0
    for i in a:
        sum+=i*i
    return sum
def func(a,b):
    i=0
    while i<len(a):
        a[i].insert(0,1)
        i+=1
    x = np.array(a)
    y=np.array(b)
    m, n = np.shape(x)
    theta = np.zeros(n)
    theta = PA(x, y, theta)
    return theta
print func([[-1,1], [0,-1],[10,1]], [1,-1,1])
