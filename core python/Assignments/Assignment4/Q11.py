# Take input
num = int(input("Enter a number: "))

# Store original number
original = num
sum = 0

# Check each digit
while num > 0:
    digit = num % 10

    # Calculate factorial
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    num = num // 10

# Check Strong Number
if sum == original:
    print("Strong Number")
else:
    print("Not a Strong Number")