import scipy
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline


#  cubic spline interpolation using direct fucntions

x = [1,2,3,7,10]
y= [10 , 23, 12 , 5 , 56]
f =interp1d(x,y,kind='cubic')
g =interp1d(x,y,kind='quadratic')
h = interp1d(x,y, kind='linear')
p=f(5)
print(p)
x1_new= np.linspace(0,10,100)
x_new = np.array([1,2,3,4,5,6,7,8,9,10])
y_new= np.array([])
y2_new= np.array([])
i = CubicSpline(x, y, bc_type='natural')        # cubic spline 
y3_new = np.array([])                           
for e in x1_new:
    y3_new = np.append(y3_new,i(e))
for e in x_new:
    y_new=np.append(y_new,f(e))
y1_new = np.array([])
for e in x_new:
    y1_new = np.append(y1_new,g(e))
for e in x_new:
    y2_new = np.append(y2_new,h(e))
plt.subplot(3,1,1)
plt.plot(x_new,y_new)
plt.subplot(3,1,2)
plt.plot(x1_new,y3_new)
plt.subplot(3,1,3)
plt.plot(x_new,y2_new)
plt.show()

