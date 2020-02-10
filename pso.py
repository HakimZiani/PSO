#PSO: Particle swarm optimization
#By Hakim Ziani
# In this exemple the program find the Min, You can switch it easily 
import time
from math import sin
import random
import matplotlib.pylab as plt
import numpy as np
#a function that retrun a list of every first element of list
def extract(list,i):
    return [l[i] for l in list ]

#Number of particls
N=100
#Number of iterations
M=100
#----------
a=-1
b=2
#----------
#Create a list of list which will contain the particles
s=a+np.random.rand(N,2)*(b-a)
# The objective fucntion
obj = lambda x,y: -((1-x)**2+100*(y-x**2)**2)
gbest=-99999
pbest=s
#parameters:
c1=0.1
r1=0.1
r2=0.2
c2=0.5
w=0.5
#first velocity
vel=[1,0.1]
#-------------
fig=plt.figure(1)
plt.ion()
for i in range(0,M):
    #setting the Global best (xbest,ybest)
    for j in range(0,N):
        if  obj(pbest[j][0],pbest[j][1]) >gbest:
            gbest=obj(pbest[j][0],pbest[j][1])
            xbest=pbest[j][0]
            ybest=pbest[j][1]
    #print(extract(s,0),extract(s,1))
    print(xbest,ybest)
    plt.cla()
    plt.plot(extract(s,0),extract(s,1),'bo')
    plt.plot(xbest,ybest,marker='s',color="red")
    plt.xlim(-1,3)
    plt.ylim(-1,3)
    plt.draw()
    plt.pause(0.05)
    for j in range(0,N):
        #Calculating the velocity
        x=w*vel[0]+c1*r1*(pbest[j][0]-s[j][0])+c2*r2*(xbest-s[j][0])
        y=w*vel[1]+c1*r1*(pbest[j][1]-s[j][1])+c2*r2*(ybest-s[j][1])
        vel=[x,y]
        #Updating the particles
        s[j]=[vel[0]+s[j][0],vel[1]+s[j][1]]
        if s[j][0]<a or s[j][0]>b or s[j][1]<a or s[j][1]>b:
            s[j]=[-1,2]
    #Updating the PBest
    for j in range(0,N):
        if obj(pbest[j][0],pbest[j][1])<obj(s[j][0],s[j][1]):
            pbest[j]=[s[j][0],s[j][1]]

plt.ioff()
plt.show()
print(gbest,xbest,ybest)
