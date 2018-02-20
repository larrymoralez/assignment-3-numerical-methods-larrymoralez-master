import math
import numpy as np
import matplotlib.pyplot as plt

import functions as fn
import numerical_solvers as ns
import output as out


def main():

    # seeding intial variables
    xmin = 0
    xmax = 10
    h = 0.01
    steps = (xmax-xmin)/(h)
    
    
    plt.figure(figsize=(14,8))

    
    
    #caculate the exact analytical solution and plot it
    X_exact, Y_exact = ns.exact(fn.exact, xmin, xmax, steps)
    out.Plot(X_exact,Y_exact, 'red')
    
    
    #caculate the numerical solutions and plot them
    X,Y = ns.rk1(fn.dy_dx, xmin, xmax, steps, math.e, h)
    out.Plot(X,Y,'#6666a3','*')
    
    X,Y = ns.rk2(fn.dy_dx, xmin, xmax, steps, math.e, h)
    out.Plot(X,Y,'#323284','D')
    
    X,Y = ns.rk4(fn.dy_dx, xmin, xmax, steps, math.e, h)
    out.Plot(X,Y,'#000066','o')
    


    
    plt.show()


if __name__== "__main__":
    main()