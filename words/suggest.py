import enchant
from sys import argv

file_name = "words"

data = []
for i in range(1, len(argv)):
	data.append(argv[i])

# f = open(file_name, 'r')
# data = f.read().split()
# f.close()

# print("data ")
# print(data)

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

for i in data:
	print()
	print(i)
	res = dct.suggest(i)
	for j in res:
		print("   ", j)