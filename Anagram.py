import os
try:
	os.remove("tmp")
except:
	None
	
from itertools import permutations

str =input("Enter Letters: ")

f = open("_dict",'r')
g = open("tmp",'w')

for word in f:
	if (len(word)-1)==len(str) :
		g.write(word)

g.close
f.close
lis = []
permList = permutations(str)
for perm in list(permList):
	g = open("tmp",'r')
	k = ''.join(perm)
	if k not in lis:
		lis.append(k)
		for word in g:
			if k in word :
				if len(k)==(len(word)-1):
					print("\nAnagrams: " + word)
	g.close()
	
os.remove("tmp")
input("---------------------------------")