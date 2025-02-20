# task3.py

# Function to check if a given number is even, odd, or zero
def check_number(num):
	if num == 0:
		return "zero"
	elif num % 2 == 0:  # Else if number is evenly devisable by 2
		return "even"
	else:
		return "odd"

# Function to find and print the first 10 prime numbers using a for loop
def print_first_primes():
	num = 2  # Start the search at 2, 1 is not a prime number
	primes = []  # Create an empty list to add primes numbers to
	while len(primes) < 10:  # Run the for loop until we have 10 prime numbers
		for i in range(2, num):
			if num % i == 0:
				break # this means it is not a prime number
		else:
			primes.append(num)
		num += 1
	print(primes)

# Function to sum the numbers from 1-100
def sum():
	sum = 0
	num = 1
	while num <= 100:  # Add each number from 1-100
		sum += num 
		num += 1
	return sum
