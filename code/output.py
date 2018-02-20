import math
import numpy as np
import matplotlib.pyplot as plt

import numerical_solvers as ns


'''General functions for formatting, printing and plotting output'''


def PrintHeader():
    '''Prints header information'''
    #TODO: (Extend and edit as you see fit to help you debug your methods)
    print("x \t EXACT  \t y(Euler) \t % Error(Euler) ")
    print("--- \t ----- \t\t ----- \t\t -------------- ")


def PrintIt(x,y_e, y):
    '''Prints and formats a row of y values for a given x'''
    #TODO: (Extend and edit as you see fit to help you debug your methods)
    print("{0:4.1f} \t {1:6.10f} \t {2:6.10f} \t {3:6.3f}%".format(x, y_e, y,  ns.error(y_e, y) * 100))


def PrintAll(X,Y,Y_e):
    '''Prints debugging data to terminal'''
    #TODO: (Extend and edit as you see fit to help you debug your methods)
    PrintHeader()
    for i in range(0,len(X)):
        PrintIt(X[i], Y_e[i], Y[i])


def PrintToFile(name, path=''):
    '''Prints caculated data to file'''
     #TODO: Extend this to have the functionality to print to file (with an optional path)
     return None


def Plot(X,Y,c,m=''):
    '''Plots caculated data to chart'''
    #TODO: (Extend and edit as you see fit to help visualize your work)
    plt.plot(X,Y, 'bo', color=c, marker=m, linestyle='-')