year = float(input("请输入一个年份"))
if (year%4==0 and year%100!=0) or year%400==0:
	print("%.0f是闰年"%year)
else:
	print("%.0f是平年"%year)
