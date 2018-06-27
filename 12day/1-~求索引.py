list=["laowang","laoli","laogao","laowang","laowang"]
name=input("请输入名字")
for position,i in enumerate(list):
	if name == i:
		print(position,i)
count=0
for i in list:
	if name == i:
		print("找到了，索引是%d"%count)
	count+=1
