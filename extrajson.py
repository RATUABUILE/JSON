# import json
# a={"name":"Ronaldo","age":23,"gender":"male"}
# b=open("extrajson .json","w")
# c=json.dump(a,b,indent=3)

# import json
# a={"name":"Ronaldo","age":23,"gender":"male"}
# b=open("extrajson .json","r")
# c=json.load(b)
# print(c)

import json
a=open("extrajson .json","r")
l=json.load(a)
m=json.dumps(l,indent=1)
print(type(m))