def isPrime(a):
	for i in range(2,a//2):
		if a % i == 0:
			return -1

	return 1

def calculatePhi(a):
	if isPrime(a):
		return p-1
	else:
		print("not a prime")
		return 
def main():
	a = int(input())
	print(calculatePhi(a))


if __name__ == '__main__':
	main()