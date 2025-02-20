# task7.py
import numpy as np

# Function that takes an array of numbers and returns the mean, median, and standard deviation of that list in a tuple using numpy functions
def array_stats(array):
	return np.mean(array), np.median(array), np.std(array)
