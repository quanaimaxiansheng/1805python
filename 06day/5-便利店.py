price = float(input("商品价格"))
name = input("商品名称")
wight = float(input("商品重量"))
username = float(input("钱包余额"))
sum = username-price
print("商品价格：%.02f\n商品名称：%s\n商品重量：%.02f\n钱包余额：%.02f\n买完商品剩的钱：%.02f"%(price,name,wight,username,sum))
