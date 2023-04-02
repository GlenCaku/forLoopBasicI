#1
for x in range(0, 151):
    print(x)

#2
for x in range(5, 1001,5):
    print(x)

#3

for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

#4

    sum = 0

for x in range(1, 500001, 2):
    sum += x

print("The sum of odd integers from 0 to 500,000 is:", sum)

#5

for x in range(2018, 0,-4):
    print(x)


#6

lowNum = 1
highNum = 30
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)

