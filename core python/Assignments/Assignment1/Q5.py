#write a program to enter P,T,R , and calculate compound Interest

Principle=int(input('enter Principle:'))
Rate=int(input('enter Rate:'))
Time=int(input('enter Time:'))

CI=Principle*(1+Rate/100)**Time-Principle

print('Compound Of interest is:', CI)