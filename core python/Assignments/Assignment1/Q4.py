#write a program to Enter P,T,R and calculate simple interest

Principle=int(input('enter Principle:'))
Rate=int(input('enter Rate:'))
Time=int(input('enter Time:'))
SI=Principle*Rate*Time/100

print('simple of interrest is:', SI)