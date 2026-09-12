#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captcha)

import random

userID= input("Enter the user Id:")
Password=input("Enter the Password:")

if userID=="1234" and Password=="1234":
    
    systemcaptcha=random.randint(1000, 9999)
    print(systemcaptcha)
    
    captcha=int(input("enter the captcha:"))
    
    if captcha==systemcaptcha:
        print("Successfully login")
        
    else:
        print("Invalid captcha")
        
else:
    print("Invalid Id and Password")