def isPrime(a):
	for i in range(2,a//2):
		if a % i == 0:
			return -1

	return 1

def calculatePhi(a):
	if isPrime(a):
		return a-1
	else:
		print("not a prime")
		return 

def primitiveRoots(a):
	phi = calculatePhi(a)
	print("{",end=" ")
	for i in range(1,phi):
		print("c|",end=" ")
	print("c",end=" ")
	print("}")
	for i in range(1,phi):
		print(i,end=' & ')
	print(phi)
	for i in range(1,phi+1):
		term = 1
		aList = [] 
		print(i, ": ", end=" & ")
		for j in range(1,phi+1):
			res = (i**j) % a
			print(res, end = " & ")
			aList.append(res)
		for i in range(1,len(aList)):
			if aList[0] == aList[i]:
				term += 1
		print(term)
		print("\\\\")

if __name__ == "__main__":
	primitiveRoots(23)