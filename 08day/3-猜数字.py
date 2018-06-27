print("游戏开始\n十次机会")
import random
pc = random.randint(1,100)

i = 0
while i<11:
	py = int(input("请输入你选择的数字："))
	if py>0 and py<100:

		if pc<py:
			print("你猜的数字偏大\n请重新输入")
		elif pc==py:
			print("恭喜你才对了")
		else:
			print("你猜的数字偏小\n请重新输入")
	elif py<0 or py>100:
		print("你输入的数字不支持，请重新输入")
	i+=1
