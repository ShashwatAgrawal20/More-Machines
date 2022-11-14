import string

# print(string.ascii_uppercase)


with open("message.txt") as filp:
	contents = filp.read()
	numbers = [ int(val) for val in contents.split() ]
	for number in numbers:
		modulus = number%37


		if modulus in range(26):
			print(string.ascii_uppercase[modulus], end="")

		elif modulus in range(26, 36):
			print(string.digits[modulus-26], end="")

		else:
			print("_", end="")