lt = []
print("VIP花名册".center(50,"*"))
while True: #死循环，可以多次操作
	print("1:添加信息")
	print("2:查找信息")
	print("3:修改信息")
	print("4:删除信息")
	print("5:退出系统")
	gn = int(input("请输入需要的功能:"))
	if gn == 1:#增
		a = {} #创建一个空的字典
		nam = input("请输入名字：")
		sex = input("请输入性别：")
		pho = input("请输入电话：")
		#为字典赋值数据
		a["nam"] = nam 
		a["sex"] = sex
		a["pho"] = pho
		lt.append(a) # 把字典添加到列表里
		print("添加完成")
		print(lt)
	
	elif gn == 2:#查
		nam = input("请输入要查找的名字：")
		for i in lt: # 先把列表便利为字典
				
			if nam==i["nam"]: #用输入的内容与字典的key作比较
				print("查找完成")
				print("姓名：%s\n性别：%s\n电话：%s"%(i["nam"],i["sex"],i["pho"]))
				break
	elif gn == 3:#改
		nam=input("1.修改名字")
		pho=input("2.修改电话")
		a=input("请选择：")
		
		for i in lt:
			if nam==i["nam"]:
				if a ==1:
					name=input("请输入你的新名字：")
					i["nam"]=name
					print("更改完成")
					print(lt)
				break
	elif gn == 4:#删
		nam=input("请输入你要删除的名字：")
		flag=False
		for position,i in enumerate(lt):
			if nam == i["nam"]:
				lt.pop(position)
		
			
				print("删除完成")
				print(lt)
				break
