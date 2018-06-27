import time
def print_game():
	i=0
	while True:
		i+=1
		if i%2==0:
			time.sleep(1)
			print("我爱玩游戏")
		else:
			print_aa()
def print_aa():
	print("我爱写代码")
print_game()
