def RSA(x):
	e = 11
	n = 3763
	return (x**e)%n

def decrypt(words):
	d = 331
	n = 3763
	for y in words:
		x = (y**d)%n
		print(chr(x),end=' ')

def main():
	words = [2912, 2929, 3368, 153, 3222, 3335, 153, 1222]
	decrypt(words)

if __name__ == '__main__':
	main()