# test_task1.py
import task1
import sys
import io

def test_hello_world():
	output = io.StringIO()  # Create a temporary output buffer to capture the print function output
	sys.stdout = output  # Assign the created buffer to be the system output 
	task1.hello_world()  # Call the function we are testing
	func_output = output.getvalue()  # Get the value of the buffer
	sys.stdout = sys.__stdout__  # Re-assign the standard output
	output.close()  # Close the temporary buffer

	# Make sure the function worked properly
	assert func_output.strip() == "Hello, World!"

