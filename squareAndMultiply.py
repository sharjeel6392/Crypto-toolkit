def splitExpression(expression):
	base, exponent = expression.split('^')
	exponent, mod = exponent.split('%')
	return int(base), int(exponent), int(mod)

def sqaureAndMultiply(expression):
	base, exponent, mod = splitExpression(expression)
	h = bin(exponent).lstrip('0b')
	r = 1
	n = len(h)
	for i in range(n):
		r = (r**2) % mod
		if h[i] == '1':
			r = (r*base) % mod
	
	print(expression,'= ',r,'mod',mod)