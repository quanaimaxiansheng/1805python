'''
hang=1
print("*")
i = 1
for hang in range(1,5):
	lie=1
	for lie in range(1,hang+1):
		lie+=1
	hang+=1
	print("*"*lie)
h=1
for h in range(1,5):
	l=1
	for l in range(1,hang+1):
		l-=1
	hang-=1
	print("*"*l)
'''
for i in range (1,5):
	print("(*)*i+1")
for l in range(5,10):
	print("*0"*i-1)

