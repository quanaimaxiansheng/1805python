account = 123
password = 123
i = 0 
while i<3:
	print("欢迎来到王者大陆")
	act = int(input("请输入您的账号："))
	pwd = int(input("请输入您的密码："))
	if act ==account and pwd == password:
		print("登陆成功")
		break
	else:
		print("账户或密码错误，请重新登录")
	i+=1
	
a = int(input("0.鲁班大师 1.程咬金 2.王昭君"))
print("请输入你要选择的英雄代号：")
if a!=0 or a!=1 or a!=2:
	print("游戏不支持")
	if a==0:
		print("你选择了鲁班大师，祝你游戏愉快")
	if a==1:
		print("你选择了程咬金，祝你游戏愉快")
	else:
		print("你选择了王昭君，祝你游戏愉快")

