import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.
    """
    # https://en.wikipedia.org/wiki/Coefficient_of_determination
	# R^2 = 1 - (sum(actual - predicted).squared / sum(actual - actual.avg).squared)
    """
    # YOUR CODE GOES HERE
    expected = np.mean(data)
    total_sum_of_squares = np.square(data - expected).sum()
    total_sum_of_residuals = np.square(data - predictions).sum()
    r_squared = 1 - (total_sum_of_residuals / total_sum_of_squares)
    return r_squared
