import sys
def table(p):
	for i in range(1,p):
		print(i,end = ' ')
	print('\n')
	for i in range(1,p):
		print(i,"\t| ", end = ' ')
		for j in range(1,p):
			print((i * j) % p, end = ' ')
		print("\n")

def main():
	p = int(sys.argv[1])
	table(p)

if __name__ == '__main__':
	main()