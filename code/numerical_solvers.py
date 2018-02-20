import math
import numpy as np
import matplotlib.pyplot as plt


'''Numerical Integrators'''

def error(exact, approx):
    '''
    Returns the (decimal) error for the exact and approx values.
    @param  exact - float - exact value
    @param  approx - float - numerically integrated value
    @return float - (decimal value) of the error
    '''    
    return #TODO: implement the error caculation.


def exact(df, xmin, xmax, steps,sm = 1):
    '''
    Returns numpy arrays of X and Y for the exact analytical solution
    @param  df - function - function to be solved
    @param xmin - float - min x value
    @param xmax - float - max x value
    @param steps - int - number of steps
    @param sm - int - (optional) accuracy multiplier if you want more point detail
    @return tuple - (X values, Y values)
    '''
    X = np.linspace(xmin, xmax, steps*sm+1) #add one so it does not run over.
    Y = np.zeros(len(x))
    y = df(x)
    return(X,Y)


def rk1(df, xmin, xmax, steps, y_start, h):
    '''
    Caculates the numerical integration of RK1 - Euler's method
    @param  df - function - function to be solved
    @param xmin - float - min x value
    @param xmax - float - max x value
    @param steps - int - number of steps
    @param y_start - float - first intial value for Y[0]
    @param h - float - step size
    @return tuple - (X values, Y values)
    '''

    X = np.linspace(xmin, xmax, steps * sm + 1)  # add one so it does not run over.
    Y = np.zeros(len(x))
    return (X,Y)


def rk2(df, xmin, xmax, steps, y_start, h):
    '''
    Caculates the numerical integration of RK2 -  MidPoint method
    @param  df - function - function to be solved
    @param xmin - float - min x value
    @param xmax - float - max x value
    @param steps - int - number of steps
    @param y_start - float - first intial value for Y[0]
    @param h - float - step size
    @return tuple - (X values, Y values)
    '''

    X = np.linspace(xmin, xmax, steps * sm + 1)  # add one so it does not run over.
    Y = np.zeros(len(x))
    return (X,Y)


def rk4(df, xmin, xmax, steps, y_start, h):
    '''
    Caculates the numerical integration of RK4 -  Runge-Kutta 4th order
    @param  df - function - function to be solved
    @param xmin - float - min x value
    @param xmax - float - max x value
    @param steps - int - number of steps
    @param y_start - float - first intial value for Y[0]
    @param h - float - step size
    @return tuple - (X values, Y values)
    '''

    X = np.linspace(xmin, xmax, steps * sm + 1)  # add one so it does not run over.
    Y = np.zeros(len(x))
    return (X,Y)



