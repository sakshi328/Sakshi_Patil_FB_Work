#WAP to calculate selling price of book based on cost price and discount
#Discount amount=cp*dsicount/100
#selling price = cp- discount amount
cp=float(input("Enter cost price="))
Discount=float(input("Enter discount:"))

Discount_amount=cp*Discount/100
sp=cp-Discount+Discount_amount

print("Selling price=",sp)