import numpy as np
import scipy
from scipy import linalg 
import math

#x= np.dot(np.linalg.inv(A),B)
#print(x)



x = np.array([1,3,6,10])
y = np.array([12,15,19,16])

matrix = np.zeros((12,12))

def base(x1, x2,n):
    result = math.pow((x1-x2),n)
    return result

for i in range (0,3):                     # 3 rows 
    for j in  range(0,12):
        if j!=4*i+3:
            matrix[i][j] = 0
        else :
            matrix[i][j] = 1

for i in range(3,7):                      # 3 rows 
    for j in range (0,12) :
        if int(j/4) == i-3 :
            matrix[i][j] = base(x[i-2],x[i-3],(3-j)%4)
        else :
            matrix[i][j] = 0

for i in range (7,9):                    # 2 rows
    for j in range(0,12):
        if j>=0 and j<=2 and i==7 :
            matrix[i][j]= (3-j)*base(x[1],x[0],2-j) 
        if i==7 and j==6 :
            matrix[i][j]= -1
        if j>=4 and j<=6 and i==8 :
            matrix[i][j] = (7-j)*base(x[2],x[1],6-j)
        if i==8 and j==10 :
            matrix[i][j] =-1 
        else : 
            matrix[i][j] = 0
for i in range(9,11):                    # 2 rows
    for j in range(0,12):
        if i==9 and j == 0 or i==9 and j==1 :
            matrix[i][j] = (6-4*j)*base(x[j+1],x[j],1-j) 
        if i==10 and j==4 or i==10 and j==5 :
            matrix[i][j] = (6-4*(j-4))*base(x[j-2],x[j-3],5-j)
        if i==9 and j== 5 or i==10 and j==9:
            matrix[i][j]= -1
        else :
            matrix[i][j] =0

#now we will use the "not a knot" approximation since 10 out of 12 equatios are made 


matrix[11][0] = 1                         # 2 rows
matrix[11][4] = -1
matrix[12][4] = 1
matrix[12][8] = -1



B = np.array([])
B= np.append(B,y)
B= np.delete(B,3)
C = np.array([])
C= np.append(C,y)
C=np.delete(C,0)
D= np.array([0,0,0,0,0,0])
C = np.append(C,D)
B=np.append(B,C)
Ans = np.array([])

Ans = np.dot(np.linalg.pinv(matrix),B)
print(Ans)

'''
x_new = np.linspace(1,4,1000)
y_new= np.array([])
for k in x_new: 
    y_new = np.append(y_new,f(k))



plt.pyplot(x_new,y_new)
plt.show()

'''

