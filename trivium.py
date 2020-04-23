def xor(a,b):
	if a == b:
		return 0
	else:
		return 1

def trivium(IV, key, C):
	s = []
	for i in range(1152):
		t1 = (IV[65] + (IV[90] * IV[91]) + IV[92]) % 2
		t2 = (key[68] + (key[81] * key[82]) + key[83]) % 2
		t3 = (C[65] + (C[108] * C[109]) + C[110]) % 2

		s.append((t1 + t2 + t3) % 2)

		t1 = (t1 + key[77]) % 2
		t2 = (t2 + C[86]) % 2
		t3 = (t3 + IV[68]) % 2

		IV.insert(0,t3)
		key.insert(0,t1)
		C.insert(0,t2)

		IV = IV[:93]
		key = key[:84]
		C = C[:111]
		#print("IV: ", A)
		#print("Key: ", B)
		#print("C: ", C)

	output = s[:70]
	output = ''.join(map(str,output))
	print(output)
	print(len(output))

def main():
	IV = [0] * 93
	key = [0] * 84
	c = [0] * 108 
	c = c + [1,1,1]
	#print("IV: ", IV)
	#print("Key: ", key)
	#print("C: ", c)
	trivium(IV, key, c)

if __name__ == '__main__':
	main()