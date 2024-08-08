import matplotlib.pyplot as plt

# india , bhuta , nepal in crores
pop_ind= [120, 123, 129,135,141]
pop_bhutan = [0.04,0.05,0.06,0.07,0.08]
pop_nepal = [0.5,0.9,1.5,2.1,3]

xlabel =  [2018, 2019, 2020, 2021, 2022]

plt.plot(xlabel,pop_ind,marker='o',ls = '-', color='b', label = 'India')
plt.plot(xlabel,pop_bhutan,marker='o',ls='--',color ='r', label = 'Bhutan')
plt.plot(xlabel,pop_nepal,marker='o',ls='-',color = 'g',label= 'Nepal')
plt.title('Population growth')
plt.xlabel('Years')
plt.ylabel('Population(in crores)')
plt.legend(loc= 'upper left')
plt.grid()
plt.show()




