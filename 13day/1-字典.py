'''
iq={"zihao":"18","fenggong":"20"}
id = {"name":"laoma","sex":"male","ads":"asddfgg","eth":"han"}
#增加
id["bir"]=18
print(id)
id.setdefault("abc",123)
print(id)
#删除
id.pop("abc")
print(id)
#改

id["name"]="yuxing"
print(id)

id.setdafault("mingzi":"laowang")
print(id)
#查
print(id["eth"])
print(id.get("birthday"))
#合并
id.update(iq)
print(id)
'''

list=[1,2,3,4,5,6,7]
for i in range(len(list)-1,-1,-1):
	list.pop(i)
print(list)
