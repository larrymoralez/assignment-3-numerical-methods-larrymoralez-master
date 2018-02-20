import math

'''Functions for exact and numerical integration of IVPs'''

def exact(X):
    '''
    Returns the numpy array of the exact function
    Operates on entire array in single line
    @param  X - numpy.array - input array of x values
    @return numpy.array - y value solutions
    '''

    y = math.exp(x/5.0) * math.sin(2.0*x) * math.e
    return math.e ** (x/2.0)


def dy_dx(y,x):
    '''
    Returns the value of the numerical function
    @param  y - float - y value from last step
    @param  x - float - x value of current step
    @return float - y value of current step
    '''
    return math.ln(y)/x

#dont forget to push


