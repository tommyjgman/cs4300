# test_task5.py
import task5
import sys
import io

# Function that tests the list of my favorite books
def test_favorite_books():
	books = task5.favorite_books()  # Assign the list of books to a variable
	assert isinstance(books, list)  # Ensure the variable returned by the function is a list
	assert len(books) >= 9  # Ensure each item in the list is there
	assert books[0] == ("If You Give a Mouse a Brownie", "Laura Numeroff")  # Ensure the first item is there

# Function that tests the output of the first_three_books function
def test_first_three_books():
	output = io.StringIO()  # Create a temporary output buffer to capture the print function output
	sys.stdout = output  # Assign the created buffer to be the system output 
	task5.first_three_books()  # Call the function we are testing
	func_output = output.getvalue()  # Get the value of the buffer
	sys.stdout = sys.__stdout__  # Re-assign the standard output
	output.close()  # Close the temporary buffer

	# Make sure the function worked properly
	assert func_output.strip() == "[('If You Give a Mouse a Brownie', 'Laura Numeroff'), ('If You Give a Mouse a Cookie', 'Laura Numeroff'), ('If You Give a Moose a Muffin', 'Laura Numeroff')]"

# Function that tests the dictionary to ensure it correlates the correct names to the correct IDs
def test_get_student_id():
	assert task5.get_student_id("Thomas") == 101
	assert task5.get_student_id("Jordan") == 102
	assert task5.get_student_id("Jack") == 112
	assert task5.get_student_id("Bear") == "Student does not exist"
	assert task5.get_student_id("jack") == "Student does not exist"
