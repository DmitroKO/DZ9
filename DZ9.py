import random
print("LIST")
numbers = []
lst = random.randint(3,10)

for i in range(lst):
    numbers.append(random.randint(0,9))


print(numbers)
print("-"*30)
num1 = numbers[0]
num2 = numbers[2]
num3 = numbers[-2]
lst2 = [num1,num2,num3]
print(lst2)
print("END")
print("-"*30)
