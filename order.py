def calcOrd(a):
	for i in range(1,a):
		for j in range(1,a):
			res = (i**j) % a
			if res == 1:
				print("Order of ",i, "mod ",a," \t= ",j,end="")
				break
			else:
				pass
		print("")

if __name__ == '__main__':
	calcOrd(37)