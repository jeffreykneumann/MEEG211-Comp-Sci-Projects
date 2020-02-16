import math
import matplotlib.pyplot as plt
import numpy as np

#Parameters
Vi = 40
G = 9.8
Ri = (-50.0,0.0)
Rf = (0.0,33.0)
STEPS = 50

#Calculates the 2 possible angles in radians.
a1 = (math.atan((((2*Vi**2)/(G*(Rf[0]-Ri[0]))) + (((-2*Vi**2)/(G*(Rf[0]-Ri[0])))**2-4*(1+((2*Rf[1]*Vi**2)/(G*(Rf[0]-Ri[0])**2))))**0.5)/2))
a2 = (math.atan((((2*Vi**2)/(G*(Rf[0]-Ri[0]))) - (((-2*Vi**2)/(G*(Rf[0]-Ri[0])))**2-4*(1+((2*Rf[1]*Vi**2)/(G*(Rf[0]-Ri[0])**2))))**0.5)/2))	

#Calculates the time that the object reaches point B based on which angle.
t_plus1 = ((-Vi*math.sin(a1)) + math.sqrt((Vi*math.sin(a1))**2+(2*G*(Ri[1]-Rf[1]))))/G*-1
t_plus2 = ((-Vi*math.sin(a2)) + math.sqrt((Vi*math.sin(a2))**2+(2*G*(Ri[1]-Rf[1]))))/G*-1

#Calculates array representations for the x-axis and time parametrizations of the 2 possilble trajectories
x = np.arange(Ri[0], Rf[0], (Rf[0]-Ri[0])/STEPS) # array of x values from 0 to 4*pi with increment of 0.1
t1 = np.arange(0.0, t_plus1, t_plus1/STEPS) # array of x values from 0 to 4*pi with increment of 0.1
t2 = np.arange(0.0, t_plus2, t_plus2/STEPS) # array of x values from 0 to 4*pi with increment of 0.1

#Calculates array of the y-axis of the 2 trajectories.
y1 = -0.5*G*(t1**2) + Vi*math.sin(a1)*t1
y2 = -0.5*G*(t2**2) + Vi*math.sin(a2)*t2

#Plots the graphs.
plt.plot(x, y1, 'r.') # plot y vs x with continuous line (default)
plt.plot(x, y2, 'gx') # plot y vs x with continuous line (default)

#Set-ups the plot.
plt.xlabel('x(m): distance traveled')
plt.ylabel('y(m): height')
plt.title('Oscillatory Motion of P')
plt.grid()
#plt.savefig('x-y.png') # save graph in png file
plt.show()

