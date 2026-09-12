# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_userid = "sakshi"
correct_password = "1234"

for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect User ID or Password")

else:
    print("3 attempts completed. Account blocked.")