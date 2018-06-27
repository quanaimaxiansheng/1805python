hang = 1

while hang<10:
	lie = 1
	
	while lie<hang+1:
		ji = hang*lie
		print("%d*%d=%d"%(lie,hang,ji),end="\t ")
		lie+=1
	print("")
	hang+=1 
