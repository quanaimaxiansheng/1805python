account = "123"
passwd = "123"
count = "123"
word ="123"
print("请选择游戏：")
game = input("1.王者荣耀 2.刺激战场")
if game =="1":
	acc = input("请输入账号：")
	pas = input("请输入密码：")
	if acc == account and pas == passwd:
		print("登陆成功\n欢迎来到召唤师峡谷")
	else:
		print("登陆失败")
elif game =="2":
	cnt = input("请输入账号：")
	wod = input("请输入密码：")
	if cnt == count and wod == word:
		print("登陆成功\n")
	else:
		print("登陆失败")
