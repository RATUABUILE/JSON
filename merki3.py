import json
# a={"name":"Ronaldo","age":23,"gender":"male"}
b=open("extrajson .json","r")
c=json.load(b)
d=json.dumps(c,indent=1)
print(type(d))