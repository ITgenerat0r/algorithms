# l = set()
# for i in range(0,int(input(""))):
# 	l.add(int(input("")))

# print()
# n = len(l) / 2

# while len(l) >= n:
# 	print(min(l))
# 	l.remove(min(l))
# for i in sorted(l):
# 	print(i)

st = list()
for i in range(0,int(input(""))):
	n = int(input(""))
	if not n in st:
		count = 0
		for j in st:
			if j > n:
				st.insert(count, n)
				count = 0
				break
			else:
				count += 1
		if count > 0 or len(st) == 0:
			st.append(n)

for i in st:
	print(i)







# s = ""
# for i in range(0,int(input(""))):
# 	s += " " + input("")
# print()

# for i in sorted(set(s.split())):
# 	print(i)