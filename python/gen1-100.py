import sys

with open('testin.txt', 'w') as f:
	sys.stdout = f # Change the standard output to the file we created.
	for i in range (1, 100):
		print("Write 0x4000 bytes to location 0x80000 ({:.2f} %)".format(i))
		print("Write 0x4000 bytes to location 0x80000 ({:.2f} %)".format(i+0.25))
		print("Write 0x4000 bytes to location 0x80000 ({:.2f} %)".format(i+0.5))
		print("Write 0x4000 bytes to location 0x80000 ({:.2f} %)".format(i+0.75))
	print("Write 0x4000 bytes to location 0x80000 (100.00 %)")

f.close()