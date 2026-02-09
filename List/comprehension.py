event = [x*y for x in range(1,6) for y in range(1,6) if (x*y)%2 == 0 ]
print(event)

words = ['apple', 'banana', 'cherry']
up = [word.upper() for word in words]
print(up)


divisible = [x for x in range(1,31) if x % 3 == 0]
print(divisible)

matrix = [[0 for _ in range(5)] for _ in range(5)]
print(matrix)