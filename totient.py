from coprime import phi
import sys

def main():
	number = int(sys.argv[1])
	if number > 0 :
		count, coPrimes = phi(number)
		print("phi(", number,") = ", count )

	else:
		print("Invalid input")

if __name__ == '__main__':
	main()