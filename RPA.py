import sys

def xor(result, second):
	rBin = bin(result).lstrip('0b').zfill(8)
	sBin = bin(second).lstrip('0b').zfill(8)
	resBin = ''
	for i in range(8):
		resBin += str((int(rBin[i]) +int(sBin[i]))%2)
	res = int(resBin,2)
	return res

def multiply(a, b):
    overflow = 0x100
    modulus = 0x11B
    res = 0
    while (b > 0):
        if (b & 1):
        	res = res ^ a            		
        b = b >> 1                          
        a = a << 1                          
        if (a & overflow):
        	a = a ^ modulus
    return res


def russianPeasant(first, second):
	
	result = 0
	if first % 2 != 0:
		result += second
	print(first,'\t| ', second)
	print("-----------------")
	while True:
		if first == 1:
			return result
		else:
			first = first // 2
			second = multiply(second,2)
			if first % 2 != 0:
				print(hex(first), "\t| ", hex(second))
				result = xor(result,second)
			else:
				print(first, " x\t| ", second)
			
def main():
	first = int(sys.argv[1],16)
	second = int(sys.argv[2],16)
	result = russianPeasant(first, second)
	print("--------------------")
	print("\t| ",result)
	print("Result: ", hex(result))

if __name__ == '__main__':
	main()