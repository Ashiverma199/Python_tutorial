# break - to stop the loopiteration

# continue - to stop current iteration of loop and start nextn

num =[10 , -20 , 30 , -40 , 50 , -60 , 70 , -80]

for n in num:
    if n ==30:
        continue
    print (n)


users=[]
name =''
while True:
    name= input("your name")
    if users == 'exit':
        break
    elif name in users:
        print("user already exists")
        continue
    else:
        print(name)



