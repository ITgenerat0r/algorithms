
n = input("n: ")
l = set()
for i in range(0,int(n)):
	num = input("")
	l.add(num)

print("")
print("Result")
for i in sorted(l):
	print(i)