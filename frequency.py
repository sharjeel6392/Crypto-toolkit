def frequencyOfLetters(text):
	count = 0
	dic = {}
	letters = 'abcdefghijklmnopqrstuvwxyz'
	for char in letters:
		dic[char] = 0

	for char in text:
		if char in dic:
			dic[char] += 1

	print(dic)

def main():
	text = "aaaaaa"
	frequencyOfLetters(text)

if __name__ == '__main__':
	main()