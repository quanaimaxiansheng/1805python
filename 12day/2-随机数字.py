import random

list=[]
'''
while len(list)<10:
	name=random.randint(1,50)
	for name in list:
		print("重复了")
		continue
		
		position=list.index(name)
		list.position(name)
	print(position)
'''
a=0
while len(list)<10:
	b=random.randint(1,50)
	list.append(b)
	c=list[a]
	a+=1
	if list.count(c)>1:
		list.pop()
		print("重复了！")
		a-=1
print(list)

