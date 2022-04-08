#Plots functions using matplotlib and numpy
#Author Chris Foley

from tkinter import CENTER
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#Definitions of functions
def f(n):  
    return n

def g(n): 
    return n*n

def h(n):         
    return n*n*n

#sets range of x
x = np.array([0, 4])

plt.title("Functions on variables", loc = 'left')

#plots each function
plt.plot(g(x), color = 'tab:blue')
plt.plot(f(x), color = 'tab:red')
plt.plot(h(x), color = 'tab:green')
plt.show()