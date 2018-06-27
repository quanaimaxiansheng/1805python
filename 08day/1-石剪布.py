'''
1:剪刀
2:石头
3:布
'''
import random
print("游戏3局定胜负")

a =int(input("请输入你的选择：1.剪刀 2.石头 3.布"))
i = 0
while i < 3:
	cer = random.randint(1,3)
	per   = int(input("请输入你的选择："))
	if a>=1 and a <=3:
		if (per==1 and cer==3) or (per==2 and cer==1) or (per==3 and cer==1):
			print("恭喜玩家胜利！")
		elif (per==cer):
			print("平局")
		else:
			print("电脑玩家胜利")
	else:
		print("请按照提示输入序号")
	i+=1
