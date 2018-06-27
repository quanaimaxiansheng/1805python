print("欢迎使用蜂巢快递".center(50,"*"))
lt=[]
#申明增加函数
def add():
	
		d={}
		while True:
			name=input("请输入姓名")
			if len(name)>4:
				print("格式错误，请重新输入")
				continue
			phone=input("请输入电话")
			if len(phone)!=11 or phone.startswith("1")==False:
				print("格式错误，请重新输入")
				continue
#把信息赋值给字典 并添加到列表内
			d["name"]=name
			d["phone"]=phone
			lt.append(d)
			print("新增信息成功")
			break
#申明查找函数
def find():
	print_if()

#申明修改函数
def gai():

	name=input("亲输入要更改的名字")
	flag=False
	for i in lt:
		
		if name == i["name"]:
			print("1.修改名字")
			print("2.修改电话")
			num=int(input("请选择功能"))
			if num==1:
				new_name=input("请输入新名字")
				i["name"]=new_name
				print("修改成功")
				flag = True
				break	
			if num==2:
				new_phone=input("请输入新电话")
				if len(new_phone)!=11 or new_phone.startswith("1")==False:
					print("格式错误请重新输入")
				else:
					i["phone"]=new_phone
					flag=True
					print("修改成功")
					break
	if flag==False:
		print("对不起，查无此人")

#申明取出函数
def take():
	name=input("请输入你要删除的名字")
	flag=False
	for position,i in enumerate(lt):
		if name==i["name"]:
			flag=True
			print("找到了")
			print("确认删除")
			print("取消删除")
			num_1=int(input("请做出选择"))
			if num_1==1:
				lt.pop(position)
				print("删除成功%s"%name)
			break
		elif flag==False:	
			print("查无此人")


#申明退出函数
def exit():
	pass
def print_if():
	name=input("请输入名字")
	flag = False#做个假设，假设没有
	for i in lt:
		if name==i["name"]:
			print("姓名：%s\n电话：%s"%(i["name"],i["phone"]))
			flag = True 
			break#找到跳出此循环
	if flag == False:
		print("没有相关信息")

#申明功能函数
def print_gn():
	
		print("1.新增信息")
		print("2.查找信息")
		print("3.修改信息")
		print("4.删除信息")
		print("5.退出系统")
		

#循环此调用的函数
while True:

	print_gn()#调用函数
	gn=int(input("请输入你要的功能"))

	if gn==1:
		add()
	elif gn==2:
		find()	
	elif gn==3:
		gai()
	elif gn==4:
		take()
	elif gn==5:
		break
	else:
		print("格式错误，请重新输入")
