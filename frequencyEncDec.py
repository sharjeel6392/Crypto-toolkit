def frequencyOfLetters(text):
	count = 0
	dic = {}
	letters = 'abcdefghijklmnopqrstuvwxyz'
	for char in letters:
		dic[char] = 0

	for char in text:
		if char in dic:
			dic[char] += 1
	dic = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))
	max1 = dic.pop(-1)
	print(max1)
	max2 = dic.pop(-1)
	print(max2)
	return max1, max2

def evaluateKey(max1):
	realMax = 'e'
	realMaxVal = ord(realMax) - 97
	maxVal = ord(max1) - 97
	if maxVal < realMaxVal:
		diffVal = realMaxVal - maxVal
	else:
		diffVal = maxVal - realMaxVal

	return diffVal

def decrypt(cipherText, key):
	plainText = ''
	for letters in cipherText:
		if letters == ' ' or letters == '\n':
			plainText += letters
		else:
			res = (ord(letters) - 97) - key
			if res < 0:
				res += 26
			plainText += chr(res + 97)

	return plainText

def main():
	file = open("1_1.txt")
	cipherText = ''
	
	for lines in file:
		cipherText += lines
	max1, max2 = frequencyOfLetters(cipherText)
	key = int(input("Key: "))
	while key != -1:
		plainText = decrypt(cipherText, key)
		print(plainText)
		key = int(input("Key: "))

if __name__ == '__main__':
	main()