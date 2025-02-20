# test_task3.py
import task3
import sys
import io

# Function to test the check_number function
def test_check_number():
	assert task3.check_number(0) == "zero"
	assert task3.check_number(21) == "odd"
	assert task3.check_number(2) == "even"

# Function to check the print_first_primes function
def test_print_first_primes():
	output = io.StringIO()  # Create a temporary output buffer to capture the print function output
	sys.stdout = output  # Assign the created buffer to be the system output
	task3.print_first_primes()  # Call the function we are testing
	func_output = output.getvalue()  # Get the value of the buffer
	sys.stdout = sys.__stdout__  # Re-assign the standard output
	output.close()  # Close the temporary buffer

	# Make sure the function worked properly
	assert func_output.strip() == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"

# Function to test the sum function
def test_sum():
	assert task3.sum() == 5050

