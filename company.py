#import numpy as np


"""
        INPUTS                                        OUTPUT
        - work (L)                                    - goods
        - capital (K)       --->    COMPANY    --->   - services          
        - intermediate goods

        class company():
    
    def __init__(self, input, output):
        self.input = input
        self.output = output
"""

def production_function(
L:float > 0, 
K:float > 0, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
    """
        The production function is assuming that the there is only
        one task and capital. We use Cobb-Douglas.

        # TO DO: implement a way to input variable production
        functions

        Args:
        L (float): labour (hours)
        K (float): capital (hours)
        A (float): C-D coefficent
        a (float): C-D coefficent
        b (float): C-D coefficent

        Returns:
        float: production function
    """

    return A * (L ** a) * (K ** b)

# Marginal productivity (MP)
def L_marginal_productivity(
L:float, 
K:float, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
        
    return A * a * (L ** (a - 1)) * (K ** b)

def K_marginal_productivity(
L:float, 
K:float, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
        
    return A * b * (L ** a) * (K ** (b - 1))

# Average productivity (AP)
def L_average_productivity(
L:float, 
K:float, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
        
    return A * (L ** (a - 1)) * (K ** b)

def K_average_productivity(
L:float, 
K:float, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
        
    return A * (L ** a) * (K ** (b - 1))

# MRS
def marginal_rate_sostitution(
L:float, 
K:float, 
A:float = 1, 
a:float = 0.5, 
b:float = 0.5
) -> float:
    """
        Function that describe the relationship between variation of K and L 
        that allows the same level of production
    
    """

    return - (L_marginal_productivity(L, K, A, a, b) / K_marginal_productivity(L, K, A, a, b))
