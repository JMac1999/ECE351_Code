# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:50:47 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 5                                                        #
# 9/28/2021                                                    #
# This code is for lab 5 of ECE 351.                           #
#                                                              #                                                    
################################################################

#Part 1 Task 1 Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1.2e-5 #step size
t = np.arange(0, 1.2e-3 + steps, steps) 
#plot starts at zero and finishes at 0.0012 on the x-axis

def u(t): #step function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)):
        if(t[i]<0):
            y[i]=0 #step function is 0 when t < 0
        else:
            y[i]=1 #step function is 1 when t >= 0
    return y #return outputs stored in the array

def Sine(R,L,C,t): #defined sine method from our class text
    alpha = -1/(2*R*C) #alpha for our y(t) function
    omega = (1/2)*np.sqrt((1/(R*C))**2-4*(1/(np.sqrt(L*C)))**2 + 0.1j)
    #omega value for our y(t) function
    p = alpha + omega #defined p equation from our class text
    g = 1/(R*C)*p #g value for our y(t) function
    mag_g = np.abs(g) #magnitude of g
    phase = np.angle(g) #phase angle of g
    
    H = (mag_g/(np.abs(omega)))*np.exp(alpha*t)*np.sin(np.abs(omega)*t+phase)*u(t)
    return H

R = 1000
L = 27e-3
C = 100e-9
#defined values for R, L, and C from prelab 5

H = Sine(R, L, C, t) #setting up our impulse repsonse function
plt.figure(figsize = (10,7))
#Impulse Response plot
plt.plot(t, H)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')
plt.title('Part 1 Impulse Response')

#Part 1 Task 2 Code

num = [0 , 1/(R*C) , 0] # Creates a matrix for the numerator
den = [1 , 1/(R*C) , 1/(C*L)] # Creates a matrix for the denominator

tout, hout = sig.impulse((num,den), T = t)
#copied from lab 5 handout

plt.figure(figsize = (10,7)) 
#Impulse Response plot
plt.plot(tout, hout)
plt.grid()
plt.ylabel('h(t)')
plt.xlabel('t')
plt.title('Part 1 Impulse Response using Sig.Impulse')


#Part 2 Code

tout, hout = sig.step((num,den), T = t)
#copied from lab 5 handout,, but using sig.step instead of sig.impulse

plt.figure(figsize = (10,7)) 
#Impulse Response plot
plt.plot(tout, hout)
plt.grid()
plt.ylabel('H(s)*u(s)')
plt.xlabel('t')
plt.title('Step Response of H(s)')

#Part 2 Final value theorem 
#Using the final value theorem on the transfer function will be produce a 0
#the final value theorem takes the limit of s as it goes to 0.
    