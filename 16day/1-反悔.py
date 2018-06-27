def chuang(account,password):
	a=phone(account)
	b=pwd(password)
	if a==True and b==True:
		print("创建成功")
	else:
		print("创建失败")
def denglu(account,password):
	a==phone(account)
	b==pwd(password)
	if a==True and b==False:
		print("登陆成功")
	else:
		print("登陆失败")
def phone(account):
	if len(account)==11 and account.startswith("1"):
		return True
	else:
		return 	False
def pwd(password):
	if len(password)>6:
		return True
	else:
		return False

