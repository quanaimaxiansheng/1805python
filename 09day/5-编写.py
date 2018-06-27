import random
a=random.randint(1,100)

count=0
for i in range(1,11):
	b=int(input("请输入你猜的数字："))
	if b<a:
		print("你输入的数偏小")
	elif b>a:
		print("你输入的数偏大")
	else:
		print("恭喜你猜对了")
		break
	count+=1
if count==1:
	print("你猜了%d次，大神"%count)
