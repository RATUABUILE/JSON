# import json
# a={1:2,2:3,3:4}
# b=open("merki1.json","w")
# c=json.dump(a,b,indent=3)
import json
b=open("merki1.json","r")
v=json.load(b)
print(v)