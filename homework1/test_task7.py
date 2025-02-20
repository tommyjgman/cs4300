# test_task7.py
import pytest
import task7

# Function that tests the array stats function 
def test_array_stats():
	data = [10, 15, 20, 25, 30]
	mean, median, standard_deviation = task7.array_stats(data)

	assert mean == 20
	assert median == 20
	assert standard_deviation == pytest.approx(50**0.5)  # using approx to avoid float errors
