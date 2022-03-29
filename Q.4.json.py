import json
x={'4': 5, '6': 7, '1': 3,'2': 4}
a=list(x.values())
a.sort()
dict={}
for i in a:
    for j in x:
        if i==x[j]:
            dict[j]=i
            k=json.dumps(dict)
print(k)
print(type(k))
