



arr = [5, 2, 4, 6]

def sum(a):
	b = []

	if a == []:
		return 0
	else:
		return a[0] + sum(a[1:])


def count(a):
	if a == []:
		return 0
	else:
		return 1 + count(a[1:])


def mx(a, m=0):
	if a == []:
		return m
	elif a[0] > m:
		return mx(a[1:], a[0])
	else:
		return mx(a[1:], m)



def qsort_myself(a):
	# print(a)
	if len(a) < 2:
		return a
	else:
		b = a[0]
		less = []
		more = []
		for i in a[1:]:
			if i < b:
				less.append(i)
			else:
				more.append(i)
		return qsort_myself(less) + [b] + qsort_myself(more)


# print(qsort_myself(arr))

