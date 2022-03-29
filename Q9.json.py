import json
dict={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
dic={}
for i in dict:
    for j in dict[i]:
            x=input("konsa iteam chahte ho:")
            if dic[j]==x:
                print(dic)
with open("pihu.json","w") as a:
    json.dump(dict,a,indent=4)  
    # x=input("konsa iteam chahte ho:")
    # y=int(input("tum kitne iteam chahte ho:"))
    # print(x)
    # print(y)


    


        

    
