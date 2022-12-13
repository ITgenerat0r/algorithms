from sys import argv
from colorama import Fore, Back, Style
import colorama
colorama.init()
import enchant
import datetime

version = "v2.3"

def print_time(ps="", oc=True):
	now = datetime.datetime.now()
	if oc:
		print(now.strftime("%H:%M:%S"), ps)
	else:
		return now.strftime("%H:%M:%S")+" "+ps

start = datetime.datetime.now()

hide = False
file_name_in = "words"
file_name_out = "words.log"

print("Version", version)
print_time("Started.")

for i in argv:
	if(i == "-hide"):
		hide = True

f = open(file_name_in, 'r')
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

f = open(file_name_out, 'w')
finded_words = 0
for i in data:
	if(dct.check(i)):
		res.append(i)
		print(Fore.YELLOW)
		print(i)
		f.write(i)
		f.write("\n")
		finded_words += 1
	elif not hide:
		print(Fore.BLUE)
		print(i)
f.close()
print_time("Checked!")

print()
print(Fore.YELLOW)
print(" Output:")
for i in res:
	print(i)

print("Finded", finded_words, "words.")
print_time("Finished!")

final = datetime.datetime.now()
elapsed = final - start
print("Elapsed time: ", elapsed)
