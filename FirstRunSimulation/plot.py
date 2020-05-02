#! /usr/bin/python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
import sys

show=False

if __name__ == '__main__':

   UV='UV.dat'
   UVfileData = np.loadtxt(UV, comments='"')
   UN='UN.dat'
   UNfileData = np.loadtxt(UN, comments='"')


   UVfreq = UVfileData[:,0]
   UVdB =  UVfileData[:,1]

   UNfreq = UNfileData[:,0]
   UNfreq = UNfreq -90
   UNdB =  UNfileData[:,1]

   ### Plot
   fig = plt.figure()
   ax = plt.axes()
   ax.set_xlim(0,90)
   ax.set_ylim(-10,35)

   plt.title("Antenna pattern (1st Run)")
   plt.xlabel("Offset from axis (deg)")
   plt.ylabel("Gain (dB)")
   plt.grid(True)

   ax.plot(UVfreq, UVdB, color='red', label='E-Plane')
   ax.plot(UNfreq, UNdB, color='blue', label='H-Plane')
   ax.legend()

   if show:
       plt.show()
       sys.exit()
   plt.gcf()
   plt.savefig("FirstRunSim.png", dpi=150)
