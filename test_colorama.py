import colorama
from time import sleep
colorama.init()
# text = "000"
# print("1111111111")
# print("2222222222")
# print("3333333333")
# print("4444444444")
# print("percent --------------1")
# print("5555555555")

# # print("\033[2A!")  
# # sleep(1)
# # print("foo")      # Выводит: foo
# # print("asdf")      # Выводит: foo
# print("\033[2A"+text) 
clear_str = "          "
clear_str += clear_str
clear_str += clear_str
clear_str += clear_str
n = "0000000000"
d = "__________"
scrl = "0000000000__________"
scrl = n + scrl + d
scrl = n + scrl + d
scrl = n + scrl + d
scrl = n + scrl + d
l = len(scrl)
print()
for i in range(0, 51):
	# print(i, clear_str)
	print(str(i*2)+"%", "["+scrl[-int(l/2)-i:-i]+"]              ")
	print("\033[2A")
	if (i % 2) == 0:
		print(i, clear_str)

	sleep(0.2)
# print("\033[1A", "Done!                               ")
print("Done!")

