#Write a program to accept an integer amount from user and tell minimum number of nodes needed for representing the amount

amount=int(input("Enter amount:"))

n500= amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount // 100
amount=amount % 100

n50 = amount // 20
amount=amount % 50

n20= amount // 20
amount= amount % 20

n10= amount // 10
amount= amount % 10

total=n500 + n200+n100+n50+20+n10
print("Minimum number of notes=", total)
