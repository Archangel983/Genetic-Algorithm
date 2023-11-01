import random
print("   _____                 _   _                 _                  _ _   _               ")
print("  / ____|               | | (_)          /\   | |                (_) | | |              ")
print(" | |  __  ___ _ __   ___| |_ _  ___     /  \  | | __ _  ___  _ __ _| |_| |__  _ __ ___  ")
print(" | | |_ |/ _ \ '_ \ / _ \ __| |/ __|   / /\ \ | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \ ")
print(" | |__| |  __/ | | |  __/ |_| | (__   / ____ \| | (_| | (_) | |  | | |_| | | | | | | | |")
print("  \_____|\___|_| |_|\___|\__|_|\___| /_/    \_\_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|")
print("                                                  __/ |                                 ")
print("                                                 |___/                                 ")
input("")
print("The selected speices for the genetic crossover and mutation is 'Human'")
input("")
Mohan=(68,1.82,'White','Brown','Green')#1 male done
Viper=(71,1.81,'Brown','Black','Blue')#2 female done
Cheyvee=(99,1.54,'White','Black','Brown')
Tom=(82,1.75,'White','Blonde','Brown')
Meet=(46,1.80,'Brown','Black','Brown')
Shamirul=(79,1.80,'Brown','Black','Blue')#2 male done
Suvidha=(69,1.69,'White','Black','Brown')#1 female done
Gracy=(86,1.56,'White','Blonde','Blue')
Ushashi=(57,1.80,'Brown','Black','Brown')
Lizzo=(102,1.61,'White','Brown','Green')
masterlist=[]
a=Mohan[0]
b=Mohan[1]
b=b**2
BMI=a/b

if(BMI>18.5 and BMI<24.9):
    print("Mohan is fit")
    print("BMI: ",BMI)
    print("------------")
    masterlist.append(Mohan)
else:
    print("Mohan is not worthy")
    print("BMI: ",BMI)
c=Cheyvee[0]
d=Cheyvee[1]
d=d**2
BMI=c/d
if(BMI>18.5 and BMI<24.9):
    print("Cheyvee is fit")
    print("BMI: ",BMI)
    masterlist.append(Cheyvee)
else:
    print("Cheyvee is not worthy")
    print("BMI: ",BMI)
    print("---------------------")
e=Tom[0]
f=Tom[1]
f=f**2
BMI=e/f
if(BMI>18.5 and BMI<24.9):
    print("Tom is fit")
    print("BMI: ",BMI)
    masterlist.append(Tom)
else:
    print("Tom is not worthy")
    print("BMI: ",BMI)
    print("-----------------")
g=Meet[0]
h=Meet[1]
h=h**2
BMI=g/h
if(BMI>18.5 and BMI<24.9):
    print("Meet is fit")
    print("BMI: ",BMI)
    masterlist.append(Meet)
else:
    print("Meet is not worthy")
    print("BMI: ",BMI)
    print("------------------")
i=Shamirul[0]
j=Shamirul[1]
j=j**2
BMI=a/b
if(BMI>18.5 and BMI<24.9):
    print("Shamirul is fit")
    print("BMI: ",BMI)
    print('---------------')
    masterlist.append(Shamirul)
else:
    print("Shamirul is not worthy")
    print("BMI: ",BMI)
k=Suvidha[0]
l=Suvidha[1]
l=l**2
BMI=k/l
if(BMI>18.5 and BMI<24.9):
    print("Suvidha is fit")
    print("BMI: ",BMI)
    print("--------------")
    masterlist.append(Suvidha)
else:
    print("Suvidha is not worthy")
    print("BMI: ",BMI)
m=Gracy[0]
n=Gracy[1]
n=n**2
BMI=m/n
if(BMI>18.5 and BMI<24.9):
    print("Gracy is fit")
    print("BMI: ",BMI)
    masterlist.append(Gracy)
else:
    print("Gracy is not worthy")
    print("BMI: ",BMI)
    print("--------------")
o=Ushashi[0]
p=Ushashi[1]
p=p**2
BMI=o/p
if(BMI>18.5 and BMI<24.9):
    print("Ushashi is fit")
    print("BMI: ",BMI)
    masterlist.append(Ushashi)
else:
    print("Ushashi is not worthy")
    print("BMI: ",BMI)
    print("--------------")
q=Viper[0]
r=Viper[1]
r=r**2
BMI=q/r
if(BMI>18.5 and BMI<24.9):
    print("Viper is fit")
    print("BMI: ",BMI)
    print("--------------")
    masterlist.append(Viper)
else:
    print("Viper is not worthy")  
    print("BMI: ",BMI)  
s=Lizzo[0]
t=Lizzo[1]
t=t**2
BMI=s/t
if(BMI>18.5 and BMI<24.9):
    print("Lizzo is fit")
    print("BMI: ",BMI)
    masterlist.append(Lizzo)
else:
    print("Lizzo is not worthy")
    print("BMI: ",BMI)
    print('-------------------')

input("")
print("(The following people have determined to be fit on the basis of their BMI) ")
print("Number of people fit are: ",len(masterlist))
input("")
print("Attributes of Fit people: ")
print("The order of the traits are as follows:\nWeight (in kg), Height (in m), Skin colour, Hair Colour, Eye Colour ")
input("")
for j in range(0,len(masterlist)):
    print(masterlist[j])
#print(masterlist)
input("")

#print("Taking Mohan and Viper as 1st case of parents, Shamirul and Suvidha as 2nd case of parents, enter 1 or 2")
#s2=int(input("Taking Mohan and Viper as 1st case of parents, Shamirul and Suvidha as 2nd case of parents, enter 1 or 2: "))
s2=int(input("Case 1:  Mohan and Viper are parents \nCase 2: Shamirul and Suvidha are parents \nEnter 1 or 2: "))
list=[]
if(s2==1):

    if(masterlist[0][2]=='Black' or masterlist[3][2]=='Black'): 
        print("Black is the dominant skin colour in Mohan and Viper")
        list.append("Black skin colour")
    elif(masterlist[0][2]=='Brown' or masterlist[3][2]=='Brown'):
        print("Brown is the dominant skin colour in Mohan and Viper")
        list.append("Brown skin colour")
    elif(masterlist[0][2]=='White' or masterlist[3][2]=='White'):
        print("White is the dominant skin colour in Mohan and Viper")
        list.append("White skin colour")
    input("")
    if(masterlist[0][3]=='Black' or masterlist[3][3]=='Black'): 
        print("Black is the dominant hair colour in Mohan and Viper")
        list.append("Black hair colour")
    elif(masterlist[0][3]=='Brown' or masterlist[3][3]=='Brown'):
        print("Brown is the dominant hair colour in Mohan and Viper")
        list.append("Brown hair colour")
    else:
        print("Blonde is the dominant hair colour in Mohan and Viper")
        list.append("Blonde hair colour")
    input("")
    list3=['Brown eye colour','Green eye colour','Blue eye colour']
    sweet=random.randrange(0,3)
    list.append(list3[sweet])
    height1=(masterlist[0][1]+masterlist[3][1])/2
    list.append(height1)
    weight1=random.randint(masterlist[0][0],masterlist[3][0])
    list.append(weight1)
    print("Their child will have the following traits:")
    print(list)
    input('')
    print("The Mutated trait will be the Eye Colour")
elif(s2==2):
    
    list5=['Black skin colour','Brown skin colour','White skin colour']
    konichiwa=random.randrange(0,3)
    list.append(list5[konichiwa])
    
    if(masterlist[1][3]=='Black' or masterlist[2][3]=='Black'): 
        print("Black is the dominant hair colour in Shamirul and Suvidha")
        list.append("Black hair colour")
    elif(masterlist[1][3]=='Brown' or masterlist[2][3]=='Brown'):
        print("Brown is the dominant hair colour in Shamirul and Suvidha")
        list.append("Brown hair colour")
    else:
        print("Blonde is the dominant hair colour in Shamirul and Suvidha")
        list.append("Blonde hair colour")
    input("")
    if(masterlist[1][4]=='Brown' or masterlist[2][4]=='Brown'): 
        print("Brown is the dominant eye colour in Shamirul and Suvidha")
        list.append("Brown eye colour")
    elif(masterlist[1][4]=='Green' or masterlist[2][4]=='Green'):
        print("Green is the doominant eye colour in Shamirul and Suvidha")
        list.append("Green eye colour")
    else:
        print("Blue is the dominant eye colour in Shamirul and Suvidha")
        list.append("Blue eye colour")
    input("")
    height2=(masterlist[1][1]+masterlist[2][1])/2
    list.append(height2)
    weight2=random.randint(masterlist[2][0],masterlist[1][0])
    list.append(weight2)
    print("Their child will have the following traits:")
    print(list)
    print("The Mutated trait will be the Skin Colour")    