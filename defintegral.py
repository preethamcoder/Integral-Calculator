from sympy.utilities.lambdify import lambdify
from sympy import *
from numpy import *
from scipy.integrate import *
import math, scipy
from scipy import integrate
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import warnings
warnings.filterwarnings("ignore") 
print()
print("Enter the function you want to see graphed and INTEGRATED!")
aba = input()
abc = aba.replace("^", "**").replace("arc", "a").replace("ln", "log")
#print(aba)
# Define function g
def g(x):
    func = eval(abc)
    return func
# Create an array of x values from 0 to 10
print("Enter the lower bound: ")
low = float(input())
print("Enter the upper bound: ")
upp = float(input())
x = np.linspace(int(floor(low))-10, int(ceil(upp))+10, 200)
try:
    print("Here is the graph of the function. Close the window if you want to see the calculated integral!")
    # Get the corresponding y values from the function
    y = [g(a) for a in x]
    # Set up the plot
    fig, ax = plt.subplots()
    plt.xlabel('$x$')
    plt.ylabel("$"+aba+"$")
    plt.grid()
    # Plot x against g(x)
    plt.plot(x,y, color='orange')
    # Make the shaded region
    ix = np.linspace(low, upp)
    #print("About to create a list of all values")
    iy = [g(i) for i in ix]
    verts = [(low, 0)] + list(zip(ix, iy)) + [(upp, 0)]
    poly = Polygon(verts, facecolor='cyan')
    ax.add_patch(poly)
    plt.show()
    #print(g(x))
    ab, bc = quad(g, low, upp)
    print("The calculated integral of " +aba+" from "+str(low)+" to "+str(upp)+" is:", ab)
except:
    print("There is a part or whole of your function that has not been implemented yet. Check back later!")
    ab, bc = quad(g, low, upp)
    print("The calculated integral of " +aba+" from "+str(low)+" to "+str(upp)+" is:", ab)
