day = int(input("请输入星期几："))
if day == 1 or day == 2 or day ==3 or day ==4 or day ==5:
	aa = input("1.上午 2.下午")
	if aa == "1":
		time = int(input("请输入时间："))
		if time > 8 and time < 10:
			print("本尊正在上课")
		elif time >10 and time < 12:
			print("本尊在耍游戏")	
	else:
		shijian = int(input("请输入时间"))
		if shijian >14 and shijian < 17:
			print("又再上课")
		else:
			print("不知道在干吗")
elif day == 6:
	print("周六在教室补课")
else:
	print("休息打球逛街")
