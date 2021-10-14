# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:43:59 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 7                                                        #
# 10/19/2021                                                   #
# This code is for lab 7 of ECE 351.                           #
#                                                              #                                                    
################################################################

#Part 1 Task 1 Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#G(s)
numG = [1, 9] # Creates a matrix for the numerator
denG = [1 , -2 , -40, -64] # Creates a matrix for the denominator

#A(s)
numA = [1, 4] # Creates a matrix for the numerator
denA = [1 , 4 , 3] # Creates a matrix for the denominator

#B(s)
numB = [1, 26 , 168] # Creates a matrix for the numerator
denB = [1] # Creates a matrix for the denominator

#Part 1 Task 2
zG, pG, kG = sig.tf2zpk(numG, denG) #Using the sig function given in the handout
zA, pA, kA = sig.tf2zpk(numA, denA) #Using the sig function given in the handout
zB, pB, kB = sig.tf2zpk(numB, denB) #Using the sig function given in the handout

#I copied the print function from lab 6
print('ZG = ', zG, '\nPG = ', pG) 
print('ZA = ', zA, '\nPA = ', pA)
print('ZB = ', zB, '\nPB = ', pB)

#Part 1 Open Loop Code
#from example code given in the lab handout
numOL = sig.convolve(numG, numA)
denOL = sig.convolve(denG, denA)
print ('Numerator = ', numOL)
print ('Denominator = ', denOL)

#Part 1 Task 4 Answer
#The open loop response is not stable. It is not stable because we have poles
#on the right side of the x and y plane

#Part 1 Task 5

tout, yout = sig.step((numOL ,denOL)) #copied from lab 6 code

plt.figure(figsize = (10,7))
plt.plot(tout, yout)
plt.grid()
plt.ylabel('yout')
plt.xlabel('tout')
plt.title('Step Response of the Open-Loop Transfer Function')

#Task 5 results do support my answer from task 4 because we have poles on
#the right side of the x and y plane

#Part 2 Task 1 & 2 Code

numCL = sig.convolve(numG, numA)
denCL = sig.convolve(denG + sig.convolve(numB, numG), denA)

zCL, pCL, kCL = sig.tf2zpk(numCL, denCL) #Using the sig function given in the handout

print('Closed Loop Zeros =', zCL, '\nClosed loop Poles =', pCL, 
      '\nClosed Loop Gain =', kCL)

#Part 2 Task 3 Answer
#The closed loop resposnse is stable. We do not have any poles on the positive side.

#Part 2 Task 4
tout, yout = sig.step((numCL ,denCL)) #copied from lab 6 code

plt.figure(figsize = (10,7))
plt.plot(tout, yout)
plt.grid()
plt.ylabel('yout')
plt.xlabel('tout')
plt.title('Step Response of the Closed-Loop Transfer Function')

#Task 4 resulsts do support my answer from task 3, because we don't have poles
#on the right side of the x and y plane
