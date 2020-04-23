import sys
from chrToIntBaseZero import *
from multiInverse import multiInverse

def decrypt(y,a,b):

	chr_y = chrToInt(y)

	inv_a = multiInverse(26, a)
	chr_x = (inv_a * (chr_y - b)) % 26
	x = intToChr(chr_x)
	return x.upper()

def main():
	message = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
	a = 7
	b = 22
	for letter in message:
		if letter == " ":
			print(letter)
		else:
			x = decrypt(letter, a, b)
			print(x, end = '')

if __name__ == "__main__":
	main()