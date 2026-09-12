#Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

ticket_amount= float(input("Enter ticket amount:"))
total=0

for i in range(5):
    age=int(input("Enter age:"))
    
    if age<12:
        amount=ticket_amount-(ticket_amount*30/100)
        
    elif age > 59:
        amount=ticket_amount-(ticket_amount*50/100)
        
    else:
        amount=ticket_amount
        
    total=total+amount
    
print("total ticket amount=", total)    
