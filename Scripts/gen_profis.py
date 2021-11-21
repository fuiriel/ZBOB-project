import random
import sys
import os

DEST = "../Dane/"
LENGTH = 9

files_no = 10
from_no = 5
to_no = 20

if len(sys.argv) >= 2:
	files_no = int(sys.argv[1])
if len(sys.argv) >= 3:
	from_no = int(sys.argv[2])
if len(sys.argv) >= 4:
	to_no = int(sys.argv[3])

for i in range(1, files_no + 1):
	randomlist = random.sample(range(from_no, to_no), LENGTH)
	randomlist = list(map(lambda x: str(x), randomlist))
	listString = "\n".join(randomlist)
	with open(f'{DEST}profits_{i}.txt', 'w') as f:
		f.write(listString)