list=[5,14,23,1,7,89,100]
for i in range(0,len(list)):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list[i],list[j]=list[j],list[i]
	print(list)
# for 求索引
for p,i in enumerate(list):
	if list[p]==89:
		print("索引是%d"%p)
		break
# while 求索引
i=0
while i<len(list):
	if list[i]==89:
		print("索引是%d"%i)
	i+=1

# index 求索引
position=list.index(89)
print("索引是%d"%position)

#二分法 求索引
number=89
min=0
max=len(list)-1
center=int((min+max)/2)
if number in list:
	while True:
		if list[center]>number:
			center=center-1
		elif list[center]<number:
			center=center+1
		elif list[center]==number:
			print("索引是%d"%center)
			break
