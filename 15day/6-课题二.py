
def print_num(a,b,c,):
	d=int(input("1.+ 2.- 3.* 4./"))

	if d==1:
		print("求得值为：%0.f"%(a+b-c))
	elif d==2:
		print("求得值为：%0.f"%(a-b-c))
	elif d==3:
		print("求得值为：%0.f"%((a*b)-c))
	elif d==3:
		print("求得值为：%0.f"%((a/b)-c))
a=int(input("请输入值"))
b=int(input("请输入值"))
c=int(input("请输入值"))

print_num(a,b,c)

