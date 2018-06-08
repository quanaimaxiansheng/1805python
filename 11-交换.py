print("你好，你还在为命令遍数太多而苦恼吗？快来看看“代写服务”吧")
print("本服务支持QQ、微信、支付宝转账")
print("请输入要不要交易，请根据意向选择：")
a = int(input("1.要 2.嫑"))
print("*"*30)
aa = int(input("请输入你被罚写的遍数："))
if a == 1:
	print("欢迎光临代写服务")
	if aa >= 1 and aa <5:
		print("你好，交易价格为5元")
	elif aa >=5 and aa<10:
		print("你好，交易价格为10元")
	elif aa >=10 and aa <20:
		print("你好，交易价格为20元")
	elif aa>=20:
		print("你走！写手不同意")
	print("你好，如果价格感觉合适，本服务先结账，后服务，谢谢")
else:
	print("谢谢光临出门左拐别回头\n祝你一路顺风半路。。。")
if a == 2:
	print("亲，你好，欢迎光临代写服务于，如果感觉价格太贵还可以议价\n是否议价")
	z = int(input("1.是 2.否"))
	if z == 1 or z == 2:
		print("欢迎光临进入“把钱扣开花”界面")
		bb = int(input("请输入需要交易的遍数："))

		if bb >=1 and bb <5:
			print("亲，交易价格为4")
		elif bb >= 5 and bb < 10:
			print("亲，交易价格为8")
		elif bb >=10 and bb <20:
			print("亲，交易价格为15")
			print("你好，如果价格感觉合适，本服务先结账，后服务，谢谢")
		elif bb >= 20:
			print("遍数太多，写手受不了")
	else:
			print("你好系统识别不了，请重启按提示输入“1”“2”")
