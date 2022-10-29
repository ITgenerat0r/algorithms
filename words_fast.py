from colorama import Fore, Back, Style
import colorama
colorama.init()
import enchant
import itertools

# dct = enchant.Dict("ru_RU")
# dct = enchant.Dict("en_EN")
# pwl = enchant.request_pwl_dict('dict/en_US')
# dct = enchant.DictWithPWL('ru_RU', 'dict/ru_RU')
dct = enchant.DictWithPWL('en_EN', 'dict/en_EN')
# set ru-RU
# form «…\LibreOffice\share\extensions\dict-ru»
# to C:\...\Python\Python36\site-packages\enchant\data\mingw64\share\enchant\hunspell
print("Selected dictionary: ",dct.tag)

# // Задать сразу ////////////////////////////////////////////////
l = "й ц у a г ш щ з х ъ ф ы в д ж я б".split()

mask = "*****"


# // Ввести в ходе выполнения программы //////////////////////////

l = []
dt = input("  Alphabet: ")
for i in dt:
	l.append(i)

mask = input(" Type mask: ")
# ////////////////////////////////////////////////////////////////


len_mask = len(mask)


def gen(s, c = 0):
	# print(c)
	# print(s)
	res = itertools.permutations(s)
	return res

def factorial(v):
	if v < 1:
		return 0
	elif v == 1:
		return 1
	else:
		return v * factorial(v-1)

print("Stage 1")
len_alphabet = len(l)

count_generate = factorial(len_alphabet)

print("Generating", count_generate, "...")
ttt = gen(l)

print(ttt)
print()
print("Stage 2")

f = open("words.log", 'w')
count = 0
last_i = ""
last_percent = 0
for ii in ttt:
	count += 1
	percent = 100*count/count_generate
	percent -= percent % 0.0001
	if last_percent != percent:
		print(Style.RESET_ALL, percent)
		last_percent = percent
	i = ""
	for it in ii:
		i += it
	if len_mask > 0:
		i = i[:len_mask]
		if i == last_i:
			continue
		else:
			last_i = i
			# input("pause for debug info")
	k = True
	# print(Fore.RED, mask[mask_len-1])
	if len(i) == len_mask or (len(i) > len_mask-1 and len_mask>0 and mask[len_mask-1]=='+'):
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
	elif len_mask == 0:
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