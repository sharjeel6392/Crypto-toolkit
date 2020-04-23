def xor(a,b):
	if a == '':
		return b
	a.zfill(2)
	b.zfill(2)
	a0 = a[2]
	a1 = a[3]
	b0 = b[2]
	b1 = b[3]
	aBin = bin(int(a0,16)).lstrip('0b').zfill(4) + bin(int(a1,16)).lstrip('0b').zfill(4)
	bBin = bin(int(b0,16)).lstrip('0b').zfill(4) + bin(int(b1,16)).lstrip('0b').zfill(4)
	cBin = ''
	for i in range(8):
		cBin += str((int(aBin[i]) + int(bBin[i]))%2)

	cDec = int(cBin,2)
	cHex = hex(cDec)
	if len(cHex) < 4:
		cHex += '0'
	print(cBin)
	print(cDec)
	print(cHex)

def binary(a):
	print(a)
	print(a>>1)
	print(a<<1)

if __name__ == '__main__':
	xor('0xff','0x01')
	binary(7)