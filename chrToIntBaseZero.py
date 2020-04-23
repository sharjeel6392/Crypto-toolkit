def chrToInt(letter):
	asci = ord(letter)
	diff = asci - 97
	return diff

def intToChr(diff):
	diff += 97
	asci = chr(diff)
	return asci