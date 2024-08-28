import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
bankerFromList = random.randint(0, len(friends)-1)
print(friends[bankerFromList])

print(random.choice(friends))
