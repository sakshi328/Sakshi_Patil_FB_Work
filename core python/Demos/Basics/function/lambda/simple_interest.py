SI=lambda p,r,t:(p*r*t)/100
p=int(input("Enter principle:"))
r=int(input("Enter rate:"))
t=int(input("Enter time:"))

print("Simple interest is:", SI(p,r,t))