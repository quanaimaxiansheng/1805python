account = input("请输入你的账号")
password = input("请输入你的密码")
user_name = input("请输入你的姓名")
money = int(input(" 请输入余额"))
need_money = int(input("请输入取出的金额"))
sum =int(money-need_money)
print("账号：%s\n密码：%s\n用户名：%s\n金额:%d\n取出金额：%d\n余额：%d"%(account,password,user_name,money,need_money,sum))
