# dictionary can store the data in key value pair
# example:-
# name:HARSH
#1: ordered 
#2: no duplicate
#3: changeable
#syntax :- 
myinfo =             {"name":"harsh",
                    "email":"harsh12@gmail.com",
                    "mobile":"1234512345",
                    "age":19}

myylist=["harsh","hiamshu","rishi"]
myylist.append("harsh")
myylist.append("himanshu")
myylist.append("rishi")
print(myylist)
print(type(myylist))
print(myylist["mobile"])
print(
    f"my name is {myylist["name"]},in{myylist["age"]}{myylist["email"]}and mobile no is {myylist["mobile"]}"
    )
for value in myylist.values():
    print(value)
