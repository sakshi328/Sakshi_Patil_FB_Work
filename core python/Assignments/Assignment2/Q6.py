#WAp to calculate total salary of employee based on basic, da=10% of baisc, ta=12% of basic, hra=15% of basic

basic=float(input("Enter basic salary:"))

da=basic*10/100
ta=basic*12/100
hra=basic*15/100

total_salary=basic+da+ta+hra

print("DA=", da)
print("TA=", ta)
print("hra=", hra)
print("Total salary=", total_salary)