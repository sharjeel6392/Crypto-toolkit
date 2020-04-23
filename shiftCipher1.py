def cipherToPlain(character, key):

	ordChar = ord(character) - 97
	res = ordChar - key
	if res < 0:
		res = 25 + res

	res = res % 26
	res = res + 97

	return chr(res)

def plainText(cipherText, key):
	plainText = ""
	for char in cipherText:
		text = cipherToPlain(char, key)
		plainText += text

	print(plainText)

def main():

	cipherText_1 = "nybfxymjgjxytkynrjxnybfxymjbtwxytkynrj"
	cipherText_2 = "bfxymjfljtkbnxitrnybfxymjfljtkkttqnxms"
	key = int(input("Enter the shift key: "))
	while key != "quit":
		plainText(cipherText_1,	key)
		plainText(cipherText_2, key)
		key = int(input("Enter the shift key: "))

if __name__ == "__main__":
	main()