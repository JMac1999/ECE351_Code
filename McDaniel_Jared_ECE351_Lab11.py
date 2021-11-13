# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 07:44:08 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 11                                                       #
# 11/16/2021                                                   #
# This code is for lab 11 of ECE 351.                          #
#                                                              #                                                    
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

plt.rcParams.update({ 'font.size' :14}) #font size on plots

def zplane(b,a,filename=None):
    #Plot the complex z-plane with the given transfer function
    
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import patches 
    
    #figure/plot
    
    ax = plt.subplot(1, 1, 1)
    
    #unit circle
    
    uc = patches.Circle((0,0), radius = 1, fill = False, color = 'black', 
                           ls = 'dashed')
    
    ax.add_patch(uc)
    
    #normalize the coefficients since they are < 1
    
    if np.max(b) > 1:
        kn = np.max(b)
        b = np.array(b)/float(kn)
    else:
        kn = 1
        
    if np.max(a) > 1:
        kd = np.max(a)
        a = np.array(a)/float(kd)
    else:
        kd = 1
        
    #poles and zeros
    
    p = np.roots(a)
    z = np.roots(b)
    k = kn/float(kd)
    
    #plot zeros/poles and set marker properties
    
    t1 = plt.plot(z.real, z.imag, 'o', ms = 10, label = 'Zeros')
    plt.setp(t1, markersize = 10.0, markeredgewidth = 1.0)
    
    t2 = plt.plot(p.real, p.imag, 'x', ms = 10, label = 'Poles')
    plt.setp(t2, markersize = 12.0, markeredgewidth = 3.0)
    
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.legend()
    
    #set ticks
    #r = 1.5; plt.axis('scaled'); plt.axis([-r, r, -r, r])
    #ticks = [-1, -0.5, 0.5, 1]; plt.xticks(ticks); plt.yticks(ticks)
    
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
        
    return p, z, k

#Part 3

num = [2, -40]
den = [1, -10, 16]

r, p, k = sig.residuez(num, den)

print('Residues = ', r, 'Poles = ', p, 'K = ', k)

#Part 4

z, p, k = zplane(num, den) #obtains pole-zero plot for H(z)

#Part 5

w, h = sig.freqz(num, den, worN=512, whole = True)
hmag = np.abs(h)
hangle = np.angle(h)

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(w, 20*np.log10(hmag))
plt.grid()
plt.title("Part 5 Plot")
plt.ylabel("Magnitude Response")


plt.subplot(2,1,2)
plt.plot(w/np.pi, 180/np.pi*hangle)
plt.grid()
plt.xlabel("Frequency")
plt.ylabel("Phase Response") 