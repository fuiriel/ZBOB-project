import random
import sys
import os

DEST = "../Dane/"
LENGTH = 9

files_no = 10
if len(sys.argv) == 2:
	file_no = int(sys.argv[1])

for i in range(1, files_no):
	randomlist = random.sample(range(5, 20), LENGTH)
	randomlist = list(map(lambda x: str(x*100), randomlist))
	listString = "\n".join(randomlist)
	with open(f'{DEST}profits_{i}.txt', 'w') as f:
		f.write(listString)