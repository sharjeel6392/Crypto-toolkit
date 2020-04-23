from gcd import gcd

def multiInverse(base, number):
	gcdAB = gcd(number, base)
	if gcdAB != 1:
		print("Inverse does not exist")
		return -1
	else:
		i = 1
		while True:
			if (number * i) % base == 1:
				return i
			else:
				i += 1