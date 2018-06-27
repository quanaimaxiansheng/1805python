import random
ap = 0
p=0
akm=0 
for day in range(1,31):
	for i in range(1,3):
		km=random.randint(1,50)
		if km<6:
			p == 3
		elif km>=6 and km<12:
			p == 4
		elif km>=12 and km<22:
			p == 5
		elif km>=22 and km<32:
			p == 6
		elif km >=32:
			if (km-32)/20==0:
				p=(6+(km-32)/20)
			else:
				p=6+int((km-32)/20)+1
		
		if p>100 and p<=150:
			ap==(ap-100)*0.8
		elif p>150 and p<=400:
			ap==(ap-150)*0.5
		ap=ap+p
		akm=akm+km
print("一个月乘坐%d公里,共花费%.02f元"%(akm,ap))
