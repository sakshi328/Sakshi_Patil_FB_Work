#Write a python program to find the two numbers whose product is maximum amoung all the pairs in a given list of numbers.use the python list
li = [2, 3, 5, 7, -8, -9]

num1 = li[0]
num2 = li[1]
max_product = num1 * num2

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        product = li[i] * li[j]

        if product > max_product:
            max_product = product
            num1 = li[i]
            num2 = li[j]

print("Numbers:", num1, num2)
print("Maximum product:", max_product)