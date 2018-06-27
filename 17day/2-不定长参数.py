def d_sum(a,b,*args,**kwargs):
	'''
	print(a)
	print(b)
	print(*args)
	print(**kwargs)
	'''
	while True:
		
		p=0
		for i in range(*args):
			p+=i
			
			if i>6:
				continue
	for j in range(**kwargs):
		
		z=int(j['values'])
		x=int(j['values'])
	print("和为%d"%(a+b+p+z+x))
d={"age":12,"weight":24}
t=(1,2,3,4,5,6,)
d_sum(1,2,*t,**d)

