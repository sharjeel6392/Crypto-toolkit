import sys

def leftSide(n, m):
	a = []
	b = []
	q = []
	r = []
	a.append(n)
	b.append(m)
	q.append(n//m)
	r.append(n%m)
	i = 0
	while r[i] != 0:
		i += 1
		a.append(b[i-1])
		b.append(r[i-1])
		q.append(a[i] // b[i])
		r.append(a[i] % b[i])

	a.append(b[i])
	b.append(r[i])
	return a,b,q,r

def _y(x,y,q):
	return (x-y*q)

def rightSide(a,b,q,r):
	X = []
	Y = []
	x = []
	y = []
	length = len(q)
	for _ in range(length):
		X.append(0)
		Y.append(0)
		x.append(0)
		y.append(0)
	x[length-1] = a[length]
	y[length-1] = b[length]
	X[length-1] = y[length-1]
	Y[length-1] = _y(x[length-1],y[length-1],q[length-1])
	for i in range(length-2,0,-1):
		x[i] = X[i+1]
		y[i] = Y[i+1]
		X[i] = y[i]
		Y[i] = _y(x[i],y[i],q[i])
	i -= 1
	x[i] = X[i+1]
	y[i] = Y[i+1]
	X[i] = y[i]
	Y[i] = _y(x[i],y[i],q[i])

	return X,Y,x,y

def EEA(n,m):
	a,b,q,r = leftSide(n,m)
	if a[-1] > 1 or b[-1] !=0:
		print("a\tb\tq\tr\t|\tX\tY\tx\ty")
		print("----------------------------",end="")
		print("-----------------------------------------")
		for i in range(len(q)):
			print(a[i],"\t",b[i],"\t",q[i],
				"\t",r[i],"\t|\t\t\t\t")
		print(a[i+1],"\t",b[i+1],"\t\t\t|")
		print("Multiplicative inverse does not exist")
		print("Since, gcd(",n,",",m,") = ",a[-1])
		return

	X,Y,x,y = rightSide(a,b,q,r)
	print("a\tb\tq\tr\t|\tX\tY\tx\ty")
	print("------------------------------",end="")
	print("---------------------------------------")
	for i in range(len(q)):
		print(a[i],"\t",b[i],"\t",q[i],"\t",r[i],"\t | \t"
			,X[i],"\t",Y[i],"\t",x[i],"\t",y[i])
	i += 1
	print(a[i],"\t",b[i])
	print("Multiplicative inverse of ",n," in Z",m," is: ", 
		X[0], " mod ",m, end = '')
	if X[0] < 0:
		print(" = ",X[0] + m, " mod ", m)
	print("\n")


def main():
	n = int(sys.argv[1])
	m = int(sys.argv[2])
	EEA(n,m)

if __name__ == '__main__':
	main()