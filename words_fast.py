from colorama import Fore, Back, Style
import colorama
colorama.init()
import enchant
import itertools


# dct = enchant.Dict("ru_RU")
# dct = enchant.Dict("en_EN")
# pwl = enchant.request_pwl_dict('dict/en_US')
dct = None
ru = False
en = False
try:
	dct_ru = enchant.DictWithPWL('ru_RU', 'dict/ru_RU')
	ru = True
except Exception as e:
	print(e)

try:
	dct_en = enchant.DictWithPWL('en_EN', 'dict/en_EN')
	en = True
except Exception as e:
	print(e)
dct = dct_en
if(ru ^ en):
	if en:
		dct = dct_en
	else:
		dct = dct_ru
# set ru-RU
# form «…\LibreOffice\share\extensions\dict-ru»
# to C:\...\Python\Python36\site-packages\enchant\data\mingw64\share\enchant\hunspell


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

if ru and en:
	if ord(l[0]) > 500:
		dct = dct_ru
	else:
		cdt = dct_en

stars = 0
len_mask = len(mask)
for i in mask:
	if i == '*':
		stars += 1

print("Selected dictionary: ",dct.tag)

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

percent_is_printed = False
def print_before_percent(text="", clear_len = 50, step_back = 1, percent_is_printed=True):
	clear_str = "     "
	while len(clear_str) < clear_len:
		clear_str += "     "
	if percent_is_printed:
		print("\033["+str(int(step_back))+"A", text, clear_str)
	else:
		print(text)
	percent_is_printed = False

print("Stage 1")
len_alphabet = len(l)
print("Alphabet size: ", Fore.RED, len_alphabet, Style.RESET_ALL, "characters")
print("Unknown characters: ", Fore.RED, stars, Style.RESET_ALL)
count_generate = factorial(len_alphabet)
if stars > len_alphabet:
	print(Fore.RED, "mask oversized Alphabet!", Style.RESET_ALL)
	raise "Error!"

print("Generating", Fore.RED, count_generate, Style.RESET_ALL, "...")
ttt = gen(l)

print()
print("Stage 2")

f = open("words.log", 'w')
scrl = "00000000000000000000000000000000000000000000000000"
scrl += "__________________________________________________"
len_scrl = len(scrl)
count = 0
last_i = ""
last_percent = 0
is_continue = False
for ii in ttt:
	count += 1
	percent = 100*count/count_generate
	pc_begin = int(percent / 2)
	if(pc_begin == 0):
		pc_end = -len_scrl
	else:
		pc_end = pc_begin
	if last_percent != percent and len_alphabet > 6:
		if is_continue:
			print("\033[2A")
			is_continue = False
		print(Style.RESET_ALL, str(percent)[:7]+"%", "["+scrl[-int(len_scrl/2)-pc_begin:-int(pc_end)]+"]  ")
		percent_is_printed = True
		last_percent = percent
	i = ""
	if len_mask > 0:
		it_t = 0
		# print()
		# print(ii)
		for it_m in range(0, len_mask):
			# print("mask[",it_m,']',mask[it_m])
			if mask[it_m] == '*':
				i += ii[it_t]
				it_t += 1
			else:
				i += mask[it_m]
		# print("debug ",i)
		if i == last_i:
			is_continue = True
			continue
		else:
			last_i = i
			# input("pause for debug info")
	if len_mask == 0:
		for it in ii:
			i += it

	# is_continue = False
	k = True
	if not is_continue:
		print("\033[2A")
	step = 1
	if len(i) == len_mask or (len(i) > len_mask-1 and len_mask>0 and mask[len_mask-1]=='+'):
		for j in range(0,len_mask):
			if mask[j] != '*':
				if mask[j] != i[j] and mask[j] != '+':
					k = False
		if k:
			if dct.check(i):
				print(Fore.YELLOW)
				print_before_percent(i, len_scrl, step, percent_is_printed)
				f.write(i + '\n')
			else:
				print(Fore.BLUE)
				print_before_percent(i, len_scrl, step, percent_is_printed)
				# f.write(i + '\n')
	elif len_mask == 0:
		if dct.check(i):
			print(Fore.YELLOW)
			print_before_percent(i, len_scrl, step, percent_is_printed)
			f.write(i + '\n')
		else:
			print(Fore.BLUE)
			print_before_percent(i, len_scrl, step, percent_is_printed)
			# f.write(i + '\n')

f.close()

print()
print(Fore.YELLOW, "Alphabet: ", dt)
print(" Mask: ", mask)
print(Fore.YELLOW, "Output: ")
f = open("words.log", 'r')
s = f.read()
while s:
	print(s)
	s = f.read()
f.close()
print(Style.RESET_ALL)
# print(rz)