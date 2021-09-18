# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 08:02:43 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 3                                                        #
# 9/21/2021                                                    #
# This code is for lab 3 of ECE 351. Lines 19-46 are from my   #
# lab 2 code.                                                  #                                                             
################################################################

#Part 1 Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1e-2 #step size
t = np.arange(0, 20 + steps, steps) 
#plot starts at zero and finishes at 10 on the x-axis

def u(t): #step function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)):
        if(t[i]<0):
            y[i]=0 #step function is 0 when t < 0
        else:
            y[i]=1 #step function is 1 when t >= 0
    return y #return outputs stored in the array

def r(t): #ramp function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)):
        if(t[i]<0):
            y[i]=0 #ramp function is 0 when t < 0
        else:
            y[i] = t[i] #ramp function equals t when t >= 0
    return y #return outputs stored in the array

def f1(t): return u(t-2)-u(t-9)
def f2(t): return np.exp(-t)*u(t)
def f3(t): return r(t-2)*(u(t-2)-u(t-3)) + r(4-t)*(u(t-3)-u(t-4))
#can't have brackets, [], in f3(t) equation or the graph won't produce

plt.figure(figsize = (10,7))
#f1(t) plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t, f1(t))
plt.grid()
plt.ylabel('f1(t)')
plt.title('Part 1 Functions')

#f2(t) plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t, f2(t))
plt.grid()
plt.ylabel('f2(t)')

#f3(t) plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t, f3(t))
plt.grid()
plt.ylabel('f3(t)')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()

#Part 2 Task 1 Code to perform a convolution

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
t1 = np.arange(0, 2*t[N-1], steps)
#create a numpy array that is a range. My interval starts at
# 0 and goes to 2*t[N-1]. The steps are values at 1e-2.    
f1=f1(t) #setting f1 = to my f1(t) function
f2=f2(t) #setting f2 = to my f2(t) function
f3=f3(t) #setting f3 = to my f3(t) function

plt.figure(figsize = (10,7))
#f1(t) plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t1, c(f1,f2))
plt.ylabel('Convolve f1(t) and f2(t)')
plt.title('Part 2 Task 1 Convolutions')
plt.grid()

#f2(t) plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t1, c(f2,f3))
plt.grid()
plt.ylabel('Convolve f2(t) and f3(t)')

#f3(t) plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t1, c(f1,f3))
plt.grid()
plt.ylabel('Convolve f1(t) and f3(t)')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()

#Part 2 Task 2, 3, and 4.



c1 = sig.convolve(f1, f2)*steps #convolution of functions 1 and 2

plt.figure(figsize = (10,7))
plt.plot(t1, c1)
plt.grid()
plt.title ('Part 2 Task 2 Plot')
plt.ylabel('Convolution of f1(t) and f2(t)')
plt.xlabel('t')
plt.show()

c2 = sig.convolve(f2, f3)*steps #convolution of functions 2 and 3

plt.figure(figsize = (10,7))
plt.plot(t1, c2)
plt.grid()
plt.title ('Part 2 Task 3 Plot')
plt.ylabel('Convolution of f2(t) and f3(t)')
plt.xlabel('t')
plt.show()

c3 = sig.convolve(f1, f3)*steps #convolution of functions 1 and 3

plt.figure(figsize = (10,7))
plt.plot(t1, c3)
plt.grid()
plt.title ('Part 2 Task 4 Plot')
plt.ylabel('Convolution of f1(t) and f3(t)')
plt.xlabel('t')
plt.show()