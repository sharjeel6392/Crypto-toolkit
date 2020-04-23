from gcd import gcd
#Eucledian Phi function: To calculate the number of coprimes a number has
def phi(m):
	count = 0
	coPrimes = []
	for n in range(1,m):
		g = gcd(n,m)
		if g == 1:
			coPrimes.append(n)
			count += 1
	return count, coPrimes