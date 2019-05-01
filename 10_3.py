# importing the required module 
import matplotlib.pyplot as plt 
import numpy as np
import math

  

def f(x, n):
    y = math.pi;
    for k in range(1, n+1):
        y = y + math.sin(k*x)*(-2/k)

    return y

#Array of the values of N i want to plot:
N = [1,2,5,10,100]

i = 1;
for n in N:
    # x axis values 
        xs = np.linspace(0.0, 4* math.pi, num=1000) #Plot with 1000 Points can be changed to change resolution

        # corresponding y axis values 
        y = np.array([f(x, n) for x in xs])

        plt.subplot(len(N), 1,i)
        # plotting the points  
        plt.plot(xs, y) 

        # naming the x axis 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis') 

        # giving a title to my graph 
        plt.title('N = ' + str(n)) 

        i = i+1

# function to show the plot 
plt.show()   


