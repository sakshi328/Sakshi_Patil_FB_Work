#1) li=[[10,20],[30,40],[50,60]]
# sum=0
# for x in li:
#     for y in x:
#         sum=sum+y
# print(sum)

# 2)
li=[5,[10,20],[30,40],[50,60]]
sum=0
for x in li:
    if type(x)==int:
        sum=sum+x
    else:
        for y in x:
            sum=sum+y
print(sum)
