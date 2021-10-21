# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:24:50 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 8                                                        #
# 10/26/2021                                                   #
# This code is for lab 8 of ECE 351.                           #
#                                                              #                                                    
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.integrate import quad

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1.2e-3 #step size
t = np.arange(0, 20 + steps, steps) 
#plot starts at zero and finishes at 20 on the x-axis

#Part 1 Task 1 Code

def b(t, k):
    return (2/(k*3.14153))*(1-np.cos(k*3.14153))*np.sin(k*(2*3.14153/8)*t)
# T = 8s
def b_k(k):
    return (2/(k*3.14153))*(1-np.cos(k*3.14153))
    
print('a_0 = ', 0)
print('a_1 = ', 0)
print('b_1 = ', b_k(1))
print('b_2 = ', b_k(2))
print('b_3 = ', b_k(3))

#Part 1 Task 2 Code and plots

def FS(t, N):
    y = 0
    for k in range(1,N+1):
        y += b(t, k)
    return y

plt.figure(figsize = (10,7))
#N = 1 plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t, FS(t,1))
plt.grid()
plt.ylabel('N = 1')
plt.title('Part 1 Task 2 Plotting Functions')

#N = 3 plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t, FS(t,3))
plt.grid()
plt.ylabel('N = 3')

#N = 15 plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t, FS(t,15))
plt.grid()
plt.ylabel('N = 15')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()


plt.figure(figsize = (10,7))
#N = 50 plot
plt.subplot(3, 1, 1) #subplot code taken from lab 1 handout. Subplot 1
plt.plot(t, FS(t,50))
plt.grid()
plt.ylabel('N = 50')
plt.title('Part 1 Task 2 Plotting Functions')

#N = 150 plot
plt.subplot(3, 1, 2) #subplot code taken from lab 1 handout. Subplot 2
plt.plot(t, FS(t,150))
plt.grid()
plt.ylabel('N = 150')

#N = 1500 plot
plt.subplot(3, 1, 3) #subplot code taken from lab 1 handout. Subplot 3
plt.plot(t, FS(t,1500))
plt.grid()
plt.ylabel('N = 1500')
plt.xlabel('t') # xlabel only needs to go on the bottom plot
plt.show()        
