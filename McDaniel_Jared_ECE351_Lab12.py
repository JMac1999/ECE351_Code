# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:49:11 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 12                                                       #
# 12/7/2021                                                    #
# This code is for lab 12 of ECE 351.                          #
#                                                              #                                                    
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import pandas as pd
import control as con
import scipy.fftpack

#Defining the initial functions that we will need to use

#defined fast fourier function from lab 9
def CleanFastFour(x, fs):

    N = len(x) # find the length of the signal
    X_fft = scipy.fftpack.fft(x) # perform the fast Fourier transform (fft)
    X_fft_shifted = scipy.fftpack.fftshift(X_fft) # shift zero frequency components
    # to the center of the spectrum
    freq = np.arange(-N/2 , N/2) * fs/N # compute the frequencies for the output
    # signal , (fs is the sampling frequency and
    # needs to be defined previously in your code
    X_mag = np.abs(X_fft_shifted)/N # compute the magnitudes of the signal
    X_phi = np.angle(X_fft_shifted) # compute the phases of the signal
    for i in range(len(X_phi)): 
        #this for loop should resolve the phase plots from Tasks 1, 2, and 3
        if (np.abs(X_mag[i]) < 1e-10): #from lab handout X_mag < 1e-10
            X_phi[i] = 0 #from lab handout X_phi = 0
    # ----- End of user defined function ----- #

    return X_mag, X_phi, freq

#workaround function from the lab handout
def make_stem(ax,x,y,color='k',style='solid',label='',linewidths=2.5,**kwargs):
    ax.axhline(x[0],x[-1],0, color = 'r')
    ax.vlines(x, 0, y, color=color, linestyles=style, label=label, linewidths=
    linewidths)
    ax.set_ylim([1.05*y.min(), 1.05*y.max()])
    
    
    
#Bandpass Filter Code

steps = 10 #small step size
w = np.arange(10, 1e6 + steps, steps) 
#omega starts at 10 rad/s and finishes at 10^6 rad/s

#I need to change these values
R = 25000
L = 127e-2
C = 5.1e-9 #typical capacitor value I found online
#R, L, C values of our RLC circuit

#RLC transfer function from lab 10
num = np.array ([1/(R*C), 0]) #numerator of the transfer function
den = np.array ([1, 1/(R*C), 1/(L*C)]) #denominator of the transfer function

plt.figure(figsize=(10,7))
#lab 10 frequency response example code
sys = con.TransferFunction(num,den)
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, plot = True)
#use _= to supress the output

plt.figure(figsize=(10,7))
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, plot = True)
#plots won't show up unless I have con.bode()
plt.xlim(17.5e2,20.5e2) #these change as my R, L, & C values change
#plt.ylim(0, -0.3)
plt.title("Position Measurement Information")


plt.figure(figsize=(10,7))
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, plot = True)
#plots won't show up unless I have con.bode()
plt.xlim(4e4,6e4) #these change as my R, L, & C values change
plt.title("Low-Frequency Vibration Noise")

plt.figure(figsize=(10,7))
_ = con.bode(sys, w, dB = True, Hz = True, deg = True, plot = True)
#plots won't show up unless I have con.bode()
plt.xlim(300,400) #these change as my R, L, & C values change
plt.title("Switching Amplifier Noise")



#Noisy Signal Starter Code from the lab handout


#load input signal
df = pd.read_csv('NoisySignal.csv')

t = df['0'].values
sensor_sig = df['1'].values

plt.figure(figsize = (10,7))
plt.plot(t, sensor_sig)
plt.grid()
plt.title('Noisy Input Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')
plt.show()


fs = 1/(t[1]-t[0])
X_mag, X_phi, freq = CleanFastFour(sensor_sig, fs) #code taken from lab 9


#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.title("CFFT for the Noisy Input Signal")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(0,400) 
plt.title("CFFT for the Low Frequency Vibration Noise")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(17.5e2,20.5e2) #these change as my R, L, & C values change
plt.title("CFFT for the Position Measurement Signal")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(4e4,6e4) #these change as my R, L, & C values change
plt.title("CFFT for the High Frequency Noise")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()



#Filtered Noisy Signal Code

#sig.bilinear and sig.lfilter was used in lab 10. 
#I copied it over into this lab

#convert the transfer function to the z-domain
#need to do this to pass the noisy signal through the RLC circuit
zeq, peq = sig.bilinear(num, den, fs=fs)  
#sig.lfilter is used to pass the noisy signal through the filter
y = sig.lfilter(zeq, peq, sensor_sig)

plt.figure(figsize=(10,7))
plt.plot(t, y)
plt.grid()
plt.title("Filtered Noisy Input Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]") 



X_mag, X_phi, freq = CleanFastFour(y, fs) #code taken from lab 9

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.title("CFFT for the Filtered Noisy Input Signal")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(0,400)
plt.title("CFFT for the Filtered Low Frequency Vibration Noise")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(17.5e2,20.5e2) #these change as my R, L, & C values change
plt.title("CFFT for the Filtered Position Measurement Signal")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show()

#to use a function as a single plot
fig, ax = plt.subplots(figsize =(10, 7)) #from 6.1.2 in the lab handout
make_stem(ax, freq, X_mag) #form 6.1.2 in the lab handout
plt.xlim(4e4,6e4) #these change as my R, L, & C values change
plt.title("CFFT for the Filtered High Frequency Noise")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.show() 

