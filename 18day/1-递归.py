def num(a):
		if a==1:
			return a
		else:
			return a*num(a-1)

ji = num(a)
print(ji)
