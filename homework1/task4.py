# task4.py

# Function to calculate the final price given an original price and a discount value, making sure the values given are numerical and are within normal range
def calculate_discount(price, discount):
	# If price and discount are proper data types
	if isinstance(price, (int, float)) and isinstance(discount, (int, float)):
		if discount < 0 or discount > 100:  # if discount is an invalid number
			raise ValueError("Discount must be a number between 0 and 100")  # throw a value error
		return round(price * (1 - (discount/100)), 2)  # else make the price calculation
	else:
		raise TypeError("The price and discount must be numbers")  # throw a type error if the given values are not numerical

