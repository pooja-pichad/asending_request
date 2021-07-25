import requests
import json
client="http://join.navgurukul.org/api/partners"
server=requests.get(client)

data=server.json()
with open("parteners_data.json","w") as f:
    json.dump(data,f,indent=4) 

serial_no=0
for i in data["data"]:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
    print("")

# user=input("what you want decending or acending order or d/a: ")
list1=[]
list2=[]
serial=0
for i in data["data"]:
    name=data["data"]
    id=data["data"]
    print(serial+1,(" -"),i["name"],(" - "),i["id"])
    list1.append(i["name"])
    list2.append(i["id"])
    serial+=1
y={}
for i in range(len(list1)):
    for k in range(len(list2)):
        y[list1[i]]=(list2[i])

print(" ")
# topic=input("enter a way you want asending/desending or a/d:")

# for asending


topic=input("enter a way you want asending/desending or a/d:")

# for asending

if topic=="a" or topic=="asending":
    list3=[]
    for x in y:
        a=y[x]
        list3.append(x)
        list3.append(a)

    n=1
    while n<len(list3):
        j=n+2
        while j<len(list3):
            if list3[n]>list3[j]:
                c=list3[n]
                list3[n]=list3[j]
                list3[j]=c
                x=a
            j+=2
        n+=2
    i=0
    m=1
    while i<len(list3):
        print(m," ",list3[i],list3[i+1])
        m+=1
        i+=2
# for desending

elif topic=="d" or topic=="desending":
    # list4=[]
    list5=[]

    for i in range(len(y)):
        max = 0
        for x in y:
            if max<y[x]:
                key=x
                max=y[x]
        list5.append(key)
        list5.append(max)
        y.pop(key)
    i=0
    s=1
    while i<len(list5):
        print(s,list5[i],list5[i+1])
        s+=1
        i+=2 
    list3=[]
    for x in y:
        a=y[x]
        list3.append(x)
        list3.append(a)

    n=1
    while n<len(list3):
        j=n+2
        while j<len(list3):
            if list3[n]>list3[j]:
                c=list3[n]
                list3[n]=list3[j]
                list3[j]=c
                x=a
            j+=2
        n+=2
    i=0
    m=1
    while i<len(list3):
        print(m," ",list3[i],list3[i+1])
        m+=1
        i+=2

