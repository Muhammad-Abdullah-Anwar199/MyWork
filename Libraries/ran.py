import random
numbers = [1, 2, 3, 4]
print(random.choices(numbers, k=3))
for _ in range(1000):
    print(random.choices(numbers, weights=[10,1,1,1], k=3))