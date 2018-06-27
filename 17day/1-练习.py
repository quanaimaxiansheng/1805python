'''
def num(a,b,c=100):
	
	return a+b
d=num(10,20)
print(d)
'''

list= []	
def shu(i):
	
	for k in range(2,i+1):
		flag=False
		for a in range(2,k):
			if k%a == 0:
				flag=True
				break
		if flag==False:
			list.append(k)
	
	return list
shu(10)
print(list)
