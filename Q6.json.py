import json
dict={"Name": "Abhishek",
"Designation": "CEO of navgurukul",
"Gender": "male","age":29}
a=open("nikki.json","w")
json.dump(dict,a,indent=4)