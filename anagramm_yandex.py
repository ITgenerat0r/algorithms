str1 = input("")
str2 = input("")
d1 = {}
d2 = {}

for i in str1:
	if i in d1.keys():
		d1[i] += 1
	else:
		d1[i] = 1

for i in str2:
	if i in d2.keys():
		d2[i] += 1
	else:
		d2[i] = 1

if d1 == d2:
	print(1)
else:
	print(0)