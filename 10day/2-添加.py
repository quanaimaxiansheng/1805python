stus = []#定一个空列表 来装输入的名字

while True:

    fun = int(input("0-----退出系统 1---添加 2--删除 3---改 4---查"))

    if fun == 1:

        name = input("请输入名字")

        stus.append(name)

    elif fun == 2:

        '''

        先查一下你在不在列表当中，如果在，就可以删，不在提示不存在     

        '''

        name = input("请输入你要删除的名字")

        if name in stus:#如果True 一定在

            stus.remove(name)

        else:

            print("查无此人")
	elif fun == 3:
		name=input("请输入你的名字：")
		if name in stus:
			b=input("请输入你要改的新名字：")
			b=stus.index(name)
			stus[b]=name
			
		else:
			print("你输入的名字不存在")
	print(stus)
	elif fun == 4:
		name=input("请输入你想要查找的名字：")
		if name in stus:
			b=stus.index[name]
			print("你要查找的是：%s"%name)	
			print(name)
	elif fun ==0:
		print("退出系统")
		break
