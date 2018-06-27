'''
riqi = "20180622"
year = riqi[0:4]
month = riqi[4:6]
day = riqi[6:8]
'''

def p_qiqi(year,month,day):
	d_month=[1,3,5,7,8,10,12]
	x_month=[4,6,9,11]
	sum_day=0
	for i in range(1,month):
		if i in d_month:
			sum_day+=31
		elif i in x_month:
			sum_day+=30
		elif i ==2:
			if (i%4==0 and i%100!=0) or i%400==0:
				sum_day+=29
			else:
				sum_day+=28
	sum_day+=day
	print("今天是一年的第%d天"%sum_day)	
riqi = "20180622"
year = int(riqi[0:4])
month = int(riqi[4:6])
day = int(riqi[6:8])
p_qiqi(year,month,day)
