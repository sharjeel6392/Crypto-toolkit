import math

def hexToDec(a):
	return int(a,16)

def hexToBin(a):
	return bin(int(a,16)).replace("0b","").zfill(8)

def decToBin(a):
	return bin(a).replace("0b","").zfill(8)

def decToHex(a):
	return hex(a).replace("0x","")

def binToDec(a):
	x = int(a,2)
	x = str(x).zfill(4)
	return x

def binToHex(a):
	d = binToDec(a)	
	return decToHex(d)


def matrix(content):
	s = []
	for item in content:
		if item == '\n' or item == '\t':
			pass
		else:
			s.append(item)
	newS = []
	for i in range(0,len(s),2):
		newS.append(s[i]+s[i+1])
	print(len(newS))
	mat = []
	for i in range(len(newS)//16):
		start = i *16
		end = start+16
		l = newS[start:end]
		mat.append(l)
	return mat

def decXor(a,b):
	binaryA = decToBin(a)
	binaryB = decToBin(b)
	binaryC = ""
	for i in range(8):
		A = int(binaryA[i])
		B = int(binaryB[i])
		C = (A+B)%2
		C = str(C)
		binaryC += C
	decC = binToDec(binaryC)
	return decC

def hexXor(a,b):
	binaryA = hexToBin(a)
	binaryB = hexToBin(b)
	binaryC = ''
	for i in range(8):
		A = int(binaryA[i])
		B = int(binaryB[i])
		C = (A+B)%2
		C = str(C)
		binaryC += C
	hexC = binToHex(binaryC)
	return hexC

def sBox(mat):
	count = 0
	for i in range(16):
		for j in range(16):
			for k in range(16):
				for l in range(16):
					first = int(str(i) + str(j))
					second = int(str(k) + str(l))
					if first != second:
						#s(x+y) = s(x) + s(y)
						leftIndex = decXor(first,second)
						l1 = leftIndex[:2]
						l2 = leftIndex[2:]
						left = mat[l1][l2]
						r1 = k
						r2 = l
						sr1 = mat[r1//10][r1%10]
						sr2 = mat[r2//10][r2%10]
						right = hexXor(sr1,sr2)
						if left == right:
							count += 1
	return count


def main():
	f = open('s.txt','r')
	content = f.read()
	mat = matrix(content)
	print(mat)
	count = sBox(mat)
	print("Count = ",count)
	print("Percentage: ", (count/256)*100)

if __name__ == '__main__':
	main()