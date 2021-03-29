

def ps(x1, y1, x2, y2):
	return (abs(x2-x1)**2+abs(y2-y1)**2)**0.5

graph = {}
towns = []

for it in range(0, int(input(''))):
	a, b = input('').split()
	towns.append([int(a), int(b)])
	
for town in towns:
	print(town)
print(towns)

