# task5.py

# Function that returns a list of my favorite books including their title and author
def favorite_books():
	return [("If You Give a Mouse a Brownie", "Laura Numeroff"),
		("If You Give a Mouse a Cookie", "Laura Numeroff"),
		("If You Give a Moose a Muffin", "Laura Numeroff"),
		("If You Give a Pig a Pancake", "Laura Numeroff"),
		("If You Take a Mouse to the Movies", "Laura Numeroff"),
		("If You Take a Mouse to School", "Laura Numeroff"),
		("If You Give a Pig a Party", "Laura Numeroff"),
		("If You Give a Cat a Cupcake", "Laura Numeroff"),
		("If You Give a Dog a Donut", "Laura Numeroff")
	]

# Function that uses list slicing to print the first three books in the list
def first_three_books():
	print(favorite_books()[:3])

# Function that creates a dictionary that represents a basic student database, including names and their corresponding student IDs. Function takes in the name of a student (case sensitive) and returns their ID if found.
def get_student_id(name):
	students = {
	"Thomas": 101,
	"Jordan": 102,
	"Jimmy": 103,
	"Jenna": 104,
	"Nick": 105,
	"Adam": 106,
	"Alex": 107,
	"Spencer": 108,
	"Allen": 109,
	"Lincoln": 110,
	"Carson": 111,
	"Jack": 112
	}

	return students.get(name, "Student does not exist")
