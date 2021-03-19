# from colorama import Fore, Back, Style
# import colorama
# colorama.init()

# dct = enchant.Dict("en_US")

l = ['a', 's', 's']
mask = "c"

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
	# print(mask[len(mask)-1])
	if len(i) == len(mask) or (len(i) > len(mask)-1 and len(mask)>0 and mask[len(mask)-1]=='+'):
		for j in range(0,len(mask)):
			if mask[j] != '*':
				if mask[j] != i[j] and mask[j] != '+':
					k = False
		if k:
			print(i)
	elif len(mask) == 0:
		print(i)


# print(rz)