import json
s={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=dict(sorted(s.items()))
b=open("merki4.json","w")
l=json.dump(a,b)