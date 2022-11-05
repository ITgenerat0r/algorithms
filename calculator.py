from sys import argv
import subprocess
from subprocess import PIPE
import os

fname = "calc_executor.vbs"
resfname = "calc_result"
if len(argv) > 1:
	# print(argv [1])


	data = 'Set FSO = CreateObject("Scripting.FileSystemObject")\r\n'
	data += 'Set f = FSO.CreateTextFile("'+resfname+'", True)\r\n'
	data += 'f.WriteLine('+argv[1]+')\r\n'
	data += 'f.Close\r\n'


	f = open(fname, 'w')
	f.write(data)
	f.close()



	process = subprocess.Popen(fname, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
	code = process.wait()
	os.remove(fname)
	if os.path.exists(resfname):
		f = open(resfname , "r")
		result = f.read().split()[0]
		f.close()
		os.remove(resfname)
		print(result)

