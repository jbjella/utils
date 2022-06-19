import sys
import re
import time
from percentbar import *

#https://stackoverflow.com/questions/6169217/replace-console-output-in-python
#Reads from a file, prints to a file

original = sys.stdout

with open('testout.txt', 'w') as f:
	with open('testin.txt','r') as i:
		lines=i.readlines()
		percentbar_start("Writing UBI")
		for line in lines:
			sys.stdout = f # Change the standard output to the file we created.
			sys.stdout.write(line)
			sys.stdout = original
			percent=re.findall(r'[-+]?\d+(?:\.\d*)?', line)
			percentbar_progress(float(percent[-1]))
			#time.sleep(0.05)
percentbar_end()
i.close()
f.close()