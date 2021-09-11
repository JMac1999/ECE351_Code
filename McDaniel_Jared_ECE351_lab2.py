# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:46:37 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 2                                                        #
# 9/14/2021                                                    #
# This code came from the Lab 2 pdf file. An example was given #
# for part 1. The rest of the code was my creation.            #                                                             
################################################################

#Part 1 Code

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1e-2 #step size
t = np.arange(0, 10 + steps, steps) 
#plot starts at zero and finishes at 10 on the x-axis

print('Number of elements:  len(t) =', len(t), '\nFirst Element: t[0] =', t[0],
  '\nLast Element: t[len(t) - 1] = ', t[len(t) - 1])

def f(t): #user defined function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)): #loop will be ran once
        y[i] = np.cos(t[i]) #implemented cosine function
    return y #returns output stored in the array

y = f(t) #call my created function

plt.figure(figsize = (10,7))
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t) with Good Resolution')
plt.xlabel('t')
plt.title('Part 1 Plot')


#Part 2 Code

t = np.arange(-5, 10 + steps, steps) 
#plot starts at -5 and finishes at 10 on the x-axis

#user defined functions

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

y = r(t) - r(t-3) + 5*u(t-3) - 2*u(t-6) - 2*r(t-6)

plt.figure(figsize = (10,7))
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 2 Plot')

#Part 3 Task 1 

t = np.arange(-10, 5 + steps, steps) 
#plot starts at -10 and finishes at 5 on the x-axis

def f1(t): return r(t) - r(t-3) + 5*u(t-3) - 2*u(t-6) - 2*r(t-6)
#returns created ramp and step function equation from Part 2

plt.figure(figsize = (10,7))
plt.plot(t, f1(-t)) #plots the original created equation just flipped
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 3 Time Reversal Plot')


#Part 3 Task 2

t = np.arange(-15, 15 + steps, steps) 
#plot starts at -15 and finishes at 15 on the x-axis

plt.figure(figsize = (10,7))
plt.plot(t, f1(t),label = 'f1(t)') #plots the original created equation
plt.plot(t, f1(t-4),label = 'f1(t-4') #plots original equation shifted 4 units to the right
plt.plot(t, f1(-t-4),label = 'f1(-t-4)') #flips plot and shifts 4 units to the left
plt.legend() #need this for labels to show up
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 3 Time-Shift Plot')


#Part 3 Task 3

t = np.arange(-5, 20 + steps, steps) 
#plot starts at -5 and finishes at 20 on the x-axis

plt.figure(figsize = (10,7))
plt.plot(t, f1(t),label = 'f1(t)') #plots the original created equation
plt.plot(t, f1(t/2),label = 'f1(t/2)') #plots original equation with time halved
plt.plot(t, f1(2*t),label = 'f1(2*t)') #flips plot with time doubled
plt.legend()
plt.ylim([-2,10])
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 3 Time Scale Plot')


#Part 3 Task 4 is to be completed by hand on draw.io
#add github url into my lab report

#Part 3 Task 5

t = np.arange(-5, 10 + steps, steps) 
#plot starts at -5 and finishes at 10 on the x-axis
dt = np.diff(t)
dy = np.diff(f1(t))/dt

plt.figure(figsize = (10,7))
plt.plot(t, f1(t),'--', label = "f1(t)") #plots the f1(t) equation with a dotted line
plt.plot(t[range(len(dy))], dy, label ='f1(t)/dt') 
#plots the derivative of the f1(t) equation
plt.legend()
plt.ylim([-2,10])
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 3 Derivative Plot')
