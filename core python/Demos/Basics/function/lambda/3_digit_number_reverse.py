reverse=lambda num:(num%10)*100+((num//10)%10)*10+(num//100)
num=321
print("Reverse=", reverse(num))