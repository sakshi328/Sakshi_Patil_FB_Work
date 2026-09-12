#Write a program to calculate profit or loss.
#SP>CP-profit
#sp<cp-loss
#sp==cp=NP , NL
cost_price=int(input("Enter cost price:"))
selling_price=int(input("Enter selling price:"))

if(selling_price>cost_price):
    profit=selling_price-cost_price
    print("Profit is", profit)

elif(selling_price<cost_price):
    loss=cost_price-selling_price
    print("Loss is", loss)
    
else:
    print("No Profit, no loss")