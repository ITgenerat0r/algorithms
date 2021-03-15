
l = ['a', 'b', 'c']
mask = "c*"

mask = input("Type mask: ")
def gen(s, c = 0):
	# print(c)
	# print(s)
	res = []
	if len(s) == 1:
		return s
	if len(s) < 1:
		return []
	for i in s:
		# print('i ', i)
		g = list(s)
		g.remove(i)
		# print(g)
		# print(s)
		r = gen(g, c+1)
		for j in r:
			res.append(i+j)
			if not j in res:
				res.append(j)
				# print(j)
		# print()
		# print(res)
	return res



ttt = gen(l)
print()
rz = list()
for i in ttt:
	if not i in rz:
		rz.append(i)

for i in rz:
	k = True
	if len(i) == len(mask):
		for j in range(0,len(mask)):
			if mask[j] != '*':
				if mask[j] != i[j]:
					k = False
		if k:
			print(i)
	elif len(mask) == 0:
		print(i)


# print(rz)