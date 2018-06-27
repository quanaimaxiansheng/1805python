height = float(input("请输入身高："))
width  = float(input("请输入体重："))
bmi    = width/height**2
if bmi<18.5:
	print("您的bmi的指数为%f，过轻"%bmi)
elif bmi>=18.5 and bmi <25:
	print("您的bmi的指数为%f，正常"%bmi)
elif bmi>=25 and bmi<28:
	print("你的bmi的指数为%f，肥胖"%bmi)
else:
	print("你的bmi的指数为%f，严重肥胖"%bmi)

