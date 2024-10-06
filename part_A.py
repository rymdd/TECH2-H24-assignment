import math
import numpy as np
"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
num_list = [1, 2, 3, 4, 5]

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    summa, length = 0, 0
    # Use for loop to calculate the sum of the numbers in the list and the length of the array
    for i in x:
        summa += i
        length += 1
    mean = summa / length
    mean_of_sq = 0
    # For loop to calculate the mean of squares
    for i in x:
        mean_of_sq += i ** 2 / length
    # Calculate the variance
    variance = mean_of_sq - mean ** 2
    # Return the standard deviation
    return variance ** 0.5

    

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # Use built-in functions to calculate the mean
    mean = sum(x) / len(x)
    # Return the calculated standard deviation using the built-in functions
    return math.sqrt(sum((i - mean) ** 2 for i in x) / len(x))
    
def std_numpy(x):
    """
    Compute standard deviation of x using the numpy library.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # Use numpy to calculate the standard deviation
    return np.std(x)


def show_validity(x: list) -> bool:
    """
    Check if the standard deviation calculated using the different methods are equal.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    bool
        True if the standard deviations are equal, False otherwise.
    """
    # Check if the standard deviation calculated using the different methods are equal
    return std_loops(x) == std_builtin(x) == std_numpy(x)

# Demonstrate that these functions calculate the same standard deviation
print(f"All methods calculate the same standard deviation: {show_validity(num_list)}")

# Show each method
print(f"Standard deviation with loops:{std_loops(num_list)}")
print(f"Standard deviation with built-in functions:{std_builtin(num_list)}")
print(f"Standard deviation with numpy:{std_numpy(num_list)}")
