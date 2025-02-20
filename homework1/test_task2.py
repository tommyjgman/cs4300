# test_task2.py
import task2

def test_integer():
	assert isinstance(task2.integer(), int)  # Ensure the function returns an integer

def test_float():
	assert isinstance(task2.float(), float)  # Ensure the function returns a float

def test_string():
	assert isinstance(task2.string(), str)  # Ensure the function returns a string

def test_boolean():
	assert isinstance(task2.boolean(), bool)  # Ensure the function returns an boolean

