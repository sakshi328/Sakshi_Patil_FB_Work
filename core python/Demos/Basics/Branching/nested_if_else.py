gender=input('enter gender(M/F):')
age=int(input("enter age:"))

if(gender=="F"):
    if(age >=18):
        print("Girls is eligible for marriage.")
    else:
        print('Pehele padhai kar lo.')

else:
    if(age >=21):
        print("Boy is eligible for marriage.")
    else:
        print('pehele kama lo.')