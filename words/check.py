from sys import argv
from colorama import Fore, Back, Style
import colorama
colorama.init()
import enchant


hide = False
file_name = "words"

for i in argv:
	if(i == "-hide"):
		hide = True

f = open(file_name, 'r')
data = f.read().split()
f.close()

if len(data) == 0:
	exit()

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




if ru and en:
	if ord(data[0][0]) > 500:
		dct = dct_ru
	else:
		cdt = dct_en

res = []

for i in data:
	if(dct.check(i)):
		res.append(i)
		print(Fore.YELLOW)
		print(i)
	elif not hide:
		print(Fore.BLUE)
		print(i)


print()
print(Fore.YELLOW)
print(" Output:")
for i in res:
	print(i)



