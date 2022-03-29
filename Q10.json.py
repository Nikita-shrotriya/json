import json
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=[a,b,c,d]
f=["name","designation","age","salary"]
g=["emp1","emp2","emp3","emp4"]
dict={}
i=0
while i<len(e):
    j=0
    dict1={}
    while j<len(e[i]):
        if j==0:
            dict1[f[j]]=e[i][j]
        elif j==1:
            dict1[f[j]]=e[i][j]
        elif j==2:
            dict1[f[j]]=e[i][j]
        elif j==3:
            dict1[f[j]]=e[i][j]
        j=j+1
        dict[g[i]]=dict1
    i=i+1
a=open("vedu.json","w")
json.dump(dict,a,indent=4)
