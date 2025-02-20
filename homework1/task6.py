# task6.py
import os

# Function to count the number of words in a .txt file
def file_word_count(filename):
	with open(filename, "r") as file:  # Open file in read mode
		text = file.read()  # Store contents of file in string variable
	return len(text.split())  # Use .split() to add each word to a list, and use len() to count the number of items in the list, aka the number of words in the file

# Function that dynamically generates function names for the pytest test cases based on filenames
def generate_function_name(filename):
	return f"test_word_count_{os.path.splitext(filename)[0]}"  # Remove the .txt part of the file name inorder to get a syntactically correct function name
