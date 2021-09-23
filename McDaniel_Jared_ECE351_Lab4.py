# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 08:46:06 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 4                                                        #
# 9/28/2021                                                    #
# This code is for lab 4 of ECE 351. Lines 19-66 are from my   #
# lab 3 code. Lines 71-146 are also from my lab 3 code         #                                                    
################################################################

#Part 1 Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1e-2 #step size
t = np.arange(-10, 10 + steps, steps) 
#plot starts at zero and finishes at 10 on the x-axis

def u(t): #step function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)):
        if(t[i]<0):
            y[i]=0 #step function is 0 when t < 0
        else:
            y[i]=1 #step function is 1 when t >= 0
    return y #return outputs stored in the array

f = 0.25
w = 2*np.pi*f

def h1(t): return np.exp(-2*t)*(u(t)-u(t-3))
def h2(t): return u(t-2)-u(t-6)
def h3(t): return np.cos(w*t)*u(t)
#can't have brackets, [], in f3(t) equation or the graph won't produce

plt.figure(figsize = (10,7))
#f1(t) plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t, h1(t))
plt.grid()
plt.ylabel('h1(t)')
plt.title('Part 1 Functions')

#f2(t) plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t, h2(t))
plt.grid()
plt.ylabel('h2(t)')

#f3(t) plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t, h3(t))
plt.grid()
plt.ylabel('h3(t)')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()

#Part 2 Task 1

def c(f1, f2): #defining convolution in python for f1 and f2.
    n1 = len(f1) #returns the number of elements in an array. (horizontal)
                 #returns an integer representing the items in f1 passed as
                 #an argument.
                 #length of array
    n2 = len(f2) #returns the number of elements in an array. (horizontal)
                 #returns an integer representing the items in f1 passed as
                 #an argument.
                 #length of array
    l1 = np.append(f1 , np.zeros((1, n2-1)))
    # np.append adds values to the end of a numpy array.
    # values are appended to a copy of this f1 array.
    # np.zeros defines an array of zeros. In this case, 1 is the shape of the
    # array and n2-1 is the desired data type of the array
    #causes f1 to be the same as f2
    l2 = np.append(f2 , np.zeros((1, n1-1)))
    # np.append adds values to the end of a numpy array.
    # values are appended to a copy of this f2 array.
    # np.zeros defines an array of zeros. In this case, 1 is the shape of the
    # array and n2-1 is the desired data type of the array
    #causes f2 to be the same as f1
    result = np.zeros(l1.shape) #creates an array of zeros with the l1 shape
    
    for i in range(n2+n1-2): #range creates a range of numbers that is nice
                             #for for loops
                             #adds n2 and n1((n2-1) + (n1-1))
                             #i goes through both
        result[i] = 0 #initializes all of them to be zero
        for j in range(n1): #when j is in the range of n1, if i-j+1 is > 0
                            #result[i] will ne added to the right side of the 
                            #equation.
            if (i - j + 1 > 0): 
            #if length of both functions is greater than the first function
                try:
                    result[i] += l1[j]*l2[i-j+1] 
                    #adds duration of each function
                except:
                    print(i,j)
    return result*steps #returns result value



N = len(t)  #returns the number of elements in an array. (horizontal)
            #returns an integer representing the items in t passed as an
            #argument.
t1 = np.arange(2*t[0], 2*t[N-1]+steps, steps)
#create a numpy array that is a range. My interval starts at
# 0 and goes to 2*t[N-1]. The steps are values at 1e-2.    
f1=h1(t) #setting f1 = to my f1(t) function
f2=h2(t) #setting f2 = to my f2(t) function
f3=h3(t) #setting f3 = to my f3(t) function

plt.figure(figsize = (10,7))
#f1(t) plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t1, c(f1,u(t)))
plt.ylabel('h1(t) & u(t)')
plt.title('Part 2 Task 1 Convolutions')
plt.xlim(-10,20)
plt.grid()

#f2(t) plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t1, c(f2,u(t)))
plt.xlim(-10,10)
plt.grid()
plt.ylabel('h2(t) & u(t)')

#f3(t) plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t1, c(f3,u(t)))
plt.xlim(-10,10)
plt.grid()
plt.ylabel('h1(t) & u(t)')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()

#Part 2 Task 2

y1 = ((1/2)*(1-np.exp(-2*t))*u(t))-((1/2)*(1-np.exp(-2*(t-3)))*u(t-3))
y2 = (t-2)*u(t-2)-(t-6)*u(t-6)
y3 = (1/w)*np.sin(w*t)*u(t)

plt.figure(figsize = (10,7))
#f1(t) plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t, y1)
plt.grid()
plt.xlim(-10,20)
plt.ylabel('y1(t)')
plt.title('Part 2 Hand Calculated Functions')

#f2(t) plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t, y2)
plt.grid()
plt.ylabel('y2(t)')

#f3(t) plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t, y3)
plt.grid()
plt.ylabel('y3(t)')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()