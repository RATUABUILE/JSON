import json
l=["neelam","programer",24,2400]
m=["komal","trainer",24,20000]
n=["anuradha","HR",25,40000]
p=["Abhishek","manager",29,63000]
r=[l,m,n,p]
list=['name','designation','age','salary']
f=['emp1','emp2','emp3','emp4']
x={}
i=0
while i<len(r):
    j=0
    s={}
    while j<len(r[i]):
        s[list[j]]=r[i][j]
        j+=1
    x[f[i]]=s
    i+=1
with open("merki8.json","w")as dict:
    json.dump(x,dict,indent=4)