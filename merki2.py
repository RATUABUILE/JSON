m={
    "name": "David", 
    "class": "I", 
    "age": 6
}
import json
a=open("merki2.json","w")
b=json.dump(m,a,indent=5)