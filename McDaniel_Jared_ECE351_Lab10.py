# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:04:39 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 10                                                       #
# 11/9/2021                                                    #
# This code is for lab 10 of ECE 351.                          #
#                                                              #                                                    
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import control as con

plt.rcParams.update({ 'font.size' :14}) #font size on plots

steps = 1e2 #small step size
w = np.arange(10**3, 10**6 + steps, steps) 
#omega starts at 10^3 rad/s and finishes at 10^6 rad/s

R = 1000
L = 27e-3
C = 100e-9
#R, L, C values of our RLC circuit

num = [1/(R*C), 0] #numerator of the transfer function
den = [1, 1/(R*C), 1/(L*C)] #denominator of the transfer function

#Part 1 Task 1

def magH(w):
    H = (w/(R*C))/(np.sqrt((w**4)+((((1/(R*C))**2)-(2/(L*C)))*w**2)+(1/(L*C))**2))
    return H
#Equation for |H(jw)| from the prelab

def angH(w):
    ang = (np.pi/2)-np.arctan((w/(R*C))/((-w**2)+(1/(L*C))))
    for i in range(len(w)):
        if ang[i] > np.pi/2:
            ang[i] = (ang[i]-np.pi)
    return ang*180/np.pi

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.semilogx(w, 20*np.log10(magH(w)))
plt.grid()
plt.title("Task 1 Bode Plot")
plt.ylabel("Magnitude")

plt.subplot(2,1,2)
plt.semilogx(w, angH(w))
plt.grid()
plt.xlabel("Omega")
plt.ylabel("Phase")       

#Part 1 Task 2

_,mag, angle = sig.bode((num,den),w)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.semilogx(w, mag)
plt.grid()
plt.title("Task 2 Bode Plot")
plt.ylabel("Magnitude")

plt.subplot(2,1,2)
plt.semilogx(w, angle)
plt.grid()
plt.xlabel("Omega")
plt.ylabel("Phase") 

#Part 1 Task 3
plt.figure(figsize=(10,7))

num = np.array ([1/(R*C), 0]) #numerator of the transfer function
den = np.array ([1, 1/(R*C), 1/(L*C)]) #denominator of the transfer function

sys = con.TransferFunction(num,den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, plot = True)

#Part 2
fs = 2*np.pi*50000
steps = 1/fs
t=np.arange(0, 0.01+steps, steps)

def x(t):
    return np.cos(2*np.pi*100*t) + np.cos(2*np.pi*3024*t) + np.cos(2*np.pi*50000*t)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t, x(t))
plt.grid()
plt.title("Part 2 Plot")
plt.ylabel("y(t)")

zeq, peq = sig.bilinear(num, den, fs)
y = sig.lfilter(zeq, peq, x(t))

plt.subplot(2,1,2)
plt.plot(t, y)
plt.grid()
plt.xlabel("Time")
plt.ylabel("filter signal") 

