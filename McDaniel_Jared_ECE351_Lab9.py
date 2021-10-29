# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 10:26:53 2021

@author: 12086
"""

################################################################
# Jared McDaniel                                               #
# ECE 351 Section 51                                           #
# Lab 9                                                        #
# 11/2/2021                                                    #
# This code is for lab 9 of ECE 351.                           #
#                                                              #                                                    
################################################################

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.fftpack
import matplotlib.gridspec as gridspec

fs = 1e2
steps = 1/fs
t=np.arange(0, 2, steps)

#Part 1 Task 1, 2, and 3 Code

def FastFour(x, fs):

    N = len(x) # find the length of the signal
    X_fft = scipy.fftpack.fft(x) # perform the fast Fourier transform (fft)
    X_fft_shifted = scipy.fftpack.fftshift(X_fft) # shift zero frequency components
    # to the center of the spectrum
    freq = np.arange(-N/2 , N/2) * fs/N # compute the frequencies for the output
    # signal , (fs is the sampling frequency and
    # needs to be defined previously in your code
    X_mag = np.abs(X_fft_shifted)/N # compute the magnitudes of the signal
    X_phi = np.angle(X_fft_shifted) # compute the phases of the signal
    # ----- End of user defined function ----- #

    return freq, X_mag, X_phi

#equations given in the lab handout
E1 = np.cos(2*np.pi*t)
E2 = 5*np.sin(2*np.pi*t)
E3 = 2*np.cos((2*np.pi*2*t)-2)+np.sin((2*np.pi*6*t)+3)**2

freq1, X_mag1, X_phi1 = FastFour(E1, fs)
freq2, X_mag2, X_phi2 = FastFour(E2, fs)
freq3, X_mag3, X_phi3 = FastFour(E3, fs)

#plot 1 Signal 1
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E1)
plt.title("Magnitude of a Fourier Series Signal 1")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq1, X_mag1, use_line_collection = True) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq1, X_mag1, use_line_collection = True) #from lab handout
plt.xlim(-2,2)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq1, X_phi1, use_line_collection = True) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq1, X_phi1, use_line_collection = True) #from lab handout
plt.xlim(-2,2)
plt.xlabel('f [Hz]')
plt.grid()

#plot 2 Signal 2
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E2)
plt.title("Magnitude of a Fourier Series Signal 2")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq2, X_mag2) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq2, X_mag2) #from lab handout
plt.xlim(-10,10)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq2, X_phi2) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq2, X_phi2) #from lab handout
plt.xlim(-2,2)
plt.xlabel('f [Hz]')
plt.grid()

#plot 3 Signal 3
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E3)
plt.title("Magnitude of a Fourier Series Signal 3")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq3, X_mag3) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq3, X_mag3) #from lab handout
plt.xlim(-15,15)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq3, X_phi3) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq3, X_phi3) #from lab handout
plt.xlim(-15,15)
plt.xlabel('f [Hz]')
plt.grid()

#Part 1 Task 4 Code

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

X_mag1, X_phi1, freq1 = CleanFastFour(E1, fs)
X_mag2, X_phi2, freq2 = CleanFastFour(E2, fs)
X_mag3, X_phi3, freq3 = CleanFastFour(E3, fs)

#plot 1.2 Signal 1
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E1)
plt.title("Plot 1.2 Magnitude of a Fourier Series Singal 1")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq1, X_mag1) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq1, X_mag1) #from lab handout
plt.xlim(-2,2)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq1, X_phi1) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq1, X_phi1) #from lab handout
plt.xlim(-2,2)
plt.xlabel('f [Hz]')
plt.grid()

#plot 2.2 Signal 2
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E2)
plt.title("Plot 2.2 Magnitude of a Fourier Series Signal 2")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq2, X_mag2) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq2, X_mag2) #from lab handout
plt.xlim(-10,10)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq2, X_phi2) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq2, X_phi2) #from lab handout
plt.xlim(-2,2)
plt.xlabel('f [Hz]')
plt.grid()

#plot 3.3 Signal 3
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, E3)
plt.title("Plot 3.3 Magnitude of a Fourier Series Signal 3")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq3, X_mag3) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq3, X_mag3) #from lab handout
plt.xlim(-15,15)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq3, X_phi3) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq3, X_phi3) #from lab handout
plt.xlim(-15,15)
plt.xlabel('f [Hz]')
plt.grid()

#Part 1 Task 5 code
#I started this by copying my Fourier series code from lab 8

t = np.arange(0, 16, steps) 
#plot starts at zero and finishes at 20 on the x-axis

def b(t, k):
    return (2/(k*np.pi))*(1-np.cos(k*np.pi))*np.sin(k*2*np.pi*t/8)

def FS(t, N):
    y = 0
    for k in range(1,N+1):
        y += b(t, k)
    return y

X_mag4, X_phi4, freq4 = CleanFastFour(FS(t,15), fs)

#plot 4 Fourier Series
figure1 = plt.figure(figsize = (10, 7))
spec = gridspec.GridSpec(nrows = 3, ncols = 2, figure = figure1)
figure1.add_subplot(spec[0,:])
plt.ylabel ('x(t)')
plt.xlabel('t [s]')
plt.plot(t, FS(t, 15))
plt.title("Plot 4 Magnitude of a Fourier Series From Lab 8")
plt.grid()

figure1.add_subplot(spec[1,0])
plt.ylabel ('|x(f)|')
plt.stem(freq4, X_mag4) #from lab handout
plt.grid()
figure1.add_subplot(spec[1,1])
plt.ylabel ('|x(f)|')
plt.stem(freq4, X_mag4) #from lab handout
plt.xlim(-2,2)
plt.grid()

figure1.add_subplot(spec[2,0])
plt.ylabel ('<x(t)')
plt.stem(freq4, X_phi4) #from lab handout
plt.xlabel('f [Hz]')
plt.grid()
figure1.add_subplot(spec[2,1])
plt.ylabel ('<x(t)')
plt.stem(freq4, X_phi4) #from lab handout
plt.xlim(-2,2)
plt.xlabel('f [Hz]')
plt.grid()