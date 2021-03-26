

def generate(cur, opend, closed, n):
	if len(cur) == 2 * n:
		print(cur)
		return
	if opend < n:
		generate(cur + "(", opend + 1, closed, n)
	if closed < opend:
		generate(cur + ")", opend, closed + 1, n)

def parens(n):
	generate("", 0, 0, n)

num = input("N: ")
parens(int(num))


