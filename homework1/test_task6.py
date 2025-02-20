# test_task6.py
import task6

# Function that creates pytest test cases with the custom function names
def create_test_function(filename, word_count):
	function_name = task6.generate_function_name(filename)  # Get the name of the function dynamically

	# Create a function that will check any file and test if the word count function returns the correct word count
	def test_function():
		assert task6.file_word_count(filename) == word_count

	# Set the dynamically determined name to be the function name
	test_function.__name__ = function_name
	# Make it so pytest runs the test function
	globals()[function_name] = test_function

# List of files with their expected word count
files = [("task6_read_me.txt", 104)]

# For loop to test each file in the list
for filename, word_count in files:
	create_test_function(filename, word_count)
