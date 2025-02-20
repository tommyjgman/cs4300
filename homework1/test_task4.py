# test_task4.py
import task4
import pytest

# Function to test the discount calculator function
def test_calculate_discount():
	assert task4.calculate_discount(72, 50) == 36.00  # Test with two integers as input
	assert task4.calculate_discount(39.5, 20) == 31.60  # Test with a float as the price input and an integer as the discount input
	assert task4.calculate_discount(120000, 10.5) == 107400.00  # Test with an integer as the price input and a float as the discount input
	assert task4.calculate_discount(100.00, 10.00) == 90.00  # Test with two floats as input
	assert task4.calculate_discount(100, 0) == 100.00  # Test with a zero as the discount
	assert task4.calculate_discount(100, 100) == 0.00  # Test with a zero as the price

	with pytest.raises(TypeError):
		task4.calculate_discount("100", 20)  # Check with invalid data type as price input
	with pytest.raises(TypeError):
                task4.calculate_discount(100, "20")  # Check with invalid data type as discount input
	with pytest.raises(ValueError):
                task4.calculate_discount(100, -20)  # Check with invalid range for discount input
	with pytest.raises(ValueError):
                task4.calculate_discount(100, 105)  # Check with invalid range for discount input
