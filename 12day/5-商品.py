lt=[]
while True:
	c=0
	a=int(input("请选择功能：1.增加 2.删除 3.修改 4.查找"))
	if a==1:
		b=[]
		name=input("请输入需要添加的商品：")
		price=input("请输入需要添加的价格：")
		b.append(name)
		b.append(price)
		lt.append(b)
		print(lt)
	elif a==2:
		b=[]
		name=input("请输入需要删除的商品：")
		price=input("请输入需要删除的价格：")
		lt.append(b)
		for i in lt:
			if b in i:
				lt.pop(c)
				print("已删除：",b)
				break
			else:
				print("无商品数据")
				c+=1
	
	elif a==3:
		b=input("请输入要更改的商品：")
		for i in lt:
			c=int(input("请选择、\n1.更该商品\n2.更改价格\n3.全部更改"))
			if c==1:
				d=input("请输入商品的新名字：")
				if b in i:
					lt[count][0]=d
			elif c==2:
				d=input("请输入商品的新价格：")
				if b in i:
					lt[count][1]=d
			elif c==3:
				d=input("请输入新商品的名字：")
				dd=input("请输入新商品的价格：")
				if b in i:
					lt[count][0]=d
					lt[count][1]=dd
			break
			count+=1
	elif a==4:
		b=input("请输入需要查看的商品：")
		for i in lt:

			if b == i[0]:
				print("要查找的商品%d，价格%f")
				break
	else:
		print("请按提示输入需求的编号！！！")
					
