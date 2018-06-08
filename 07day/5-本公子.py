
print("请选择性别：")
sex = input("1.男 2.女")

if sex == "1":
	height = int(input("请输入身高："))
	caifu = int(input("请输入财富："))
	face = int(input("请输入颜值："))
	if (height > 180 and caifu > 1000) and face > 90:
		print("你是高富帅！")
	else:
		print("稳住老弟，别哭")
elif sex == "2":
	yanse = input("请输入皮肤颜色：")
	money = int(input("请输入财富："))
	yan = int(input("请输入颜值："))
	if (yanse == "白色" and money > 800) and yan > 90:
		print("一枚大美女！")
	else:
		print("哈哈哈")

