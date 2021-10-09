# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:03:29 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 6                                                        #
# 10/12/2021                                                   #
# This code is for lab 5 of ECE 351.                           #
#                                                              #                                                    
################################################################

#Part 1 Task 1 Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1.2e-5 #step size
t = np.arange(0, 2 + steps, steps) 
#plot starts at zero and finishes at 2 on the x-axis

def u(t): #step function
    y=np.zeros(t.shape) #y(t) is initialized as an array of zeros
    
    for i in range(len(t)):
        if(t[i]<0):
            y[i]=0 #step function is 0 when t < 0
        else:
            y[i]=1 #step function is 1 when t >= 0
    return y #return outputs stored in the array

def y(t): #hand calculated step resonse

    return (1/2 - 1/2*np.exp(-4*t) + np.exp(-6*t))*u(t)

plt.figure(figsize = (10,7))
#Hand Calculated Step Response plot
plt.plot(t, y(t))
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Part 1 Hand Calculated Step Response')

#Part 1 Task 2 Code

num = [1, 6 , 12] # Creates a matrix for the numerator
den = [1 , 10 , 24] # Creates a matrix for the denominator

tout, yout = sig.step((num,den), T = t)

plt.figure(figsize = (10,7))
#Hand Calculated Step Response plot
plt.plot(tout, yout)
plt.grid()
plt.ylabel('yout')
plt.xlabel('tout')
plt.title('Part 1 Task 2 Sig.Step Response')

#Part 1 Task 3 Code

num = [1, 6 , 12] # Creates a matrix for the numerator
den = [1 , 10 , 24, 0] # Creates a matrix for the denominator

R, P, K = sig.residue(num, den)

print('R1 = ', R, '\nP1 = ', P)

#Part 2 Task 1 Code

steps = 1.2e-5 #step size
t = np.arange(0, 4.5 + steps, steps) 
#plot starts at zero and finishes at 2 on the x-axis

num = [25250] # Creates a matrix for the numerator
den = [1 , 18 , 218, 2036, 9085, 25250, 0] # Creates a matrix for the denominator

R, P, K = sig.residue(num, den)

print('R2 = ', R, '\nP2 = ', P)

#Part 2 Task 2 Code

def Cosine(R, P, t): #defined cosine method from the class text
    y = 0;
    for i in range(len(R)):
        mag_k = np.abs(R[i]) #magnitude of k
        phase = np.angle(R[i]) #phase angle of k
        alpha = np.real(P[i]) #alpha is the real component of P
        omega = np.imag(P[i]) #omega is the imaginary component of P
        y += mag_k*np.exp(alpha*t)*np.cos(omega*t + phase)*u(t)
    return y

plt.figure(figsize = (10,7))
#Time Domain Response plot
plt.plot(t, Cosine(R, P, t))
plt.grid()
plt.ylabel('y')
plt.xlabel('t')
plt.title('Part 2 Task 2 Time Domain Response')

#Part 2 Task 3 Code

num = [25250] # Creates a matrix for the numerator
den = [1 , 18 , 218, 2036, 9085, 25250] # Creates a matrix for the denominator

tout, yout = sig.step((num,den), T = t)
        
plt.figure(figsize = (10,7))
#Time Domain Response plot
plt.plot(tout, yout)
plt.grid()
plt.ylabel('yout')
plt.xlabel('tout')
plt.title('Part 2 Task 3 Sig.Step Response')        