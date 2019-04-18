numbers = [1,2,3]
tuples = ['Pedro', 'Geoge W Bush', 'Peter']

for i, name in zip(numbers, tuples):
    print(str(i) + ": " + name)

number = 10
numbers = []
while number >= 0:
    numbers.append(number)
    number = number-1

print(numbers[0:2])
