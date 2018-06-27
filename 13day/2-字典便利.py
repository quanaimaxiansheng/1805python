'''
list={"laowang":"san","laoma":"wu","laofeng":"er","laoyuan":"yi","laochen":"si"}
for k,v in list.items():
	print("%s键%s值"%(k,v))
for i in list.keys():
	print(i)
for i in list.values():
	print(i)
'''
list=[{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":123331,"renkou":123123}}]
for i in list:
	'''
	for a in i.keys():
		print(a)	
	for b in i.values():
		print(b)
	'''
	for k,v in i.items():
		for a,b in v.items():
			print(k,a,b)


