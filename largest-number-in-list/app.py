import random
numbers = []

while len(numbers) <= 6:
    numbers.append(random.randint(1, 5000))

max = 0

for number in numbers:
    if number > max:
        max = number

print(f'The biggest number in the list is {max}')