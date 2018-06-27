list = []
for i in range(2,101):
    fg = 0
    for j in range(2,i-1):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
		list.append(i)
print (list)
he = 0 
for i in list:
	he+=i
print("素数和是%d"he)
list.reverse()
print(list)
