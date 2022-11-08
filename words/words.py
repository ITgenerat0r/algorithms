from colorama import Fore, Back, Style
import colorama
colorama.init()
import enchant

# dct = enchant.Dict("ru_RU")
# dct = enchant.Dict("en_EN")
# pwl = enchant.request_pwl_dict('dict/en_US')
dct = enchant.DictWithPWL('ru_RU', 'dict/ru_RU')
# dct = enchant.DictWithPWL('en_EN', 'dict/en_EN')
# set ru-RU
# form «…\LibreOffice\share\extensions\dict-ru»
# to C:\...\Python\Python36\site-packages\enchant\data\mingw64\share\enchant\hunspell
print("Selected dictionary: ",dct.tag)


l = ['t', 'e', 's', 't']
mask = "c"
l = []
dt = input("  Alphabet: ")
for i in dt:
	l.append(i)


mask = input(" Type mask: ")

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

def factorial(v):
	if v < 1:
		return 0
	elif v == 1:
		return 1
	else:
		return v * factorial(v-1)

print("Stage 1")
len_alphabet = len(dt)

count_generate = factorial(len_alphabet)

print("Generating", count_generate, "...")
ttt = gen(l)
print()

print("Stage 2")
rz = list()
print("There is", len(ttt), "combinations.")
count = 0
for i in ttt:
	count += 1
	if not i in rz:
		rz.append(i)
	percent = 100*count/len(ttt)
	percent = percent - (percent%0.01)
	print(percent)

print()
print("Stage 3")

f = open("words.log", 'w')

for i in rz:
	k = True
	# print(Fore.RED, mask[len(mask)-1])
	if len(i) == len(mask) or (len(i) > len(mask)-1 and len(mask)>0 and mask[len(mask)-1]=='+'):
		for j in range(0,len(mask)):
			if mask[j] != '*':
				if mask[j] != i[j] and mask[j] != '+':
					k = False
		if k:
			if dct.check(i):
				print(Fore.YELLOW, i)
				f.write(i + '\n')
			else:
				print(Fore.BLUE, i)
	elif len(mask) == 0:
		if dct.check(i):
			print(Fore.YELLOW, i)
			f.write(i + '\n')
		else:
			print(Fore.BLUE, i)

f.close()

print()
print(Fore.YELLOW, "Output: ")
f = open("words.log", 'r')
s = f.read()
while s:
	print(s)
	s = f.read()
f.close()
print(Style.RESET_ALL)
# print(rz)