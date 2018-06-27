'''
def print_num(num):
sun=0
for i in range(num+1):
	sum+=i
print(sum)
print_num(300)		
'''
def print_num(a,b,c):
		
		
	if c==1:
		print("求得值为：%0.2f"%(a+b))
	elif c==2:
		print("求得值为：%0.2f"%(a-b))
	elif c==3:
		print("求得值为：%0.2f"%(a*b))
	else:
		print("求得值为：%0.2f"%(a/b))
		
print_num(178,140,2)
