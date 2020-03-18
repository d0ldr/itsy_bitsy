"""
imse_vimse_spindel.py   (itsy bitsy spider)

"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

number_of_positions = 200    #   positions on the straw
number_of_spiders = 5000     #   how long the spider list will become
number_of_iterations = 3000   #   I don't understand how this influence the
                            #   result. Should this be high or just the number
                            #   of positions?  

def main():
    spiders = [0] * number_of_spiders
    
    for _ in range(number_of_iterations):
        for ind in range(len(spiders) - 1):
            spiders[ind] = (new_one_step(spiders[ind]))
    result = []
    
    for i in range(number_of_positions):
        result.append(spiders.count(i))
        
    for k in range(len(result)):
        position = (len(result)-1) - k

        print("position",'{0:0=3d}'.format(position),
              "*"*math.floor(result[(len(result)-1) - k]/2))
    
    x_vals = np.array(list(range(len(result))))
    y_vals = np.array(result)
    popt, pcov = curve_fit(func, x_vals, y_vals)
    print(popt, '\n*\n', pcov)
    yy_fit = func(x_vals, popt[0],popt[1],popt[2],popt[3])
    
    plt.plot(result, '*')
    plt.plot(yy_fit)
    plt.show()
    
def func(x, a, b, c, d):
    """Exp function to fit"""
    return a*np.exp(b-c*x)+d

def new_one_step(spiders_position):
    """Move the spider one step if it's not raining"""
    if random.randint(1, 100) < 6:
        return 0
    else:
        if spiders_position == number_of_positions - 1:
            return 0
        else:
            return spiders_position + 1

if __name__ == "__main__":
    main()
