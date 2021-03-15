str1 = input("")
str2 = input("")
d1 = {}
d2 = {}
res = 0


for i in str1:
	if not i in d1:
		print("not")
		d1.append(i,0)
	else:
		d1[i] += 1
for i in str2:
	d2[i] += 1
if len(str1) == len(str2):
	r = 1
	for i in d1.keys():
		if d1[i] != d2[i]:
			r = 0
	if r:
		res = 1

print(res)