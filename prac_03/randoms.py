import random

print(random.randint(5, 20))  # line 1
# What did you see on line 1? 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# The smallest number you could have seen: 5
# The largest number you could have seen: 20

print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2? 3, 5, 7, 9
# The smallest number you could have seen: 3
# The largest number you could have seen: 9
# Could line 2 have produced a 4? No

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3? number between 2.5 and 5.5
# The smallest number you could have seen: 2.5
# The largest number you could have seen: 5.5

number = random.randint(1, 100)
print(number)
