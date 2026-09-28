from functools import reduce

# 1. Double All Numbers
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*2, nums)))  # [2, 4, 6, 8, 10]

# 2. Square All Numbers
nums = [2, 3, 4, 5]
print(list(map(lambda x: x**2, nums)))  # [4, 9, 16, 25]

# 3. Convert Strings to Integers
strs = ["10", "20", "30", "40"]
print(list(map(int, strs)))  # [10, 20, 30, 40]

# 4. Convert Names to Uppercase
names = ["john", "alice", "bob"]
print(list(map(str.upper, names)))  # ['JOHN', 'ALICE', 'BOB']

# 5. Find Length of Each Word
words = ["apple", "banana", "kiwi"]
print(list(map(len, words)))  # [5, 6, 4]

# 6. Filter Even Numbers
nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x%2==0, nums)))  # [2, 4, 6]

# 7. Filter Odd Numbers
print(list(filter(lambda x: x%2!=0, nums)))  # [1, 3, 5]

# 8. Filter Positive Numbers
nums = [-5, -2, 0, 3, 8]
print(list(filter(lambda x: x>0, nums)))  # [3, 8]

# 9. Filter Words Longer Than 4 Characters
words = ["cat", "elephant", "dog", "tiger"]
print(list(filter(lambda x: len(x)>4, words)))  # ['elephant', 'tiger']

# 10. Extract Vowels from a String
s = "programming"
print(list(filter(lambda c: c in 'aeiou', s)))  # ['o', 'a', 'i']

# 11. Sum of All Numbers
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a,b: a+b, nums))  # 15

# 12. Product of All Numbers
nums = [1, 2, 3, 4]
print(reduce(lambda a,b: a*b, nums))  # 24

# 13. Find Maximum Number
nums = [4, 10, 7, 25, 3]
print(reduce(lambda a,b: a if a>b else b, nums))  # 25

# 14. Find Minimum Number
print(reduce(lambda a,b: a if a<b else b, nums))  # 3

# 15. Join Words into a Sentence
words = ["Python", "is", "awesome"]
print(reduce(lambda a,b: a+" "+b, words))  # Python is awesome

# 16. Square Only Even Numbers
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x**2, filter(lambda x: x%2==0, nums))))  # [4, 16, 36]

# 17. Sum of Even Numbers
print(reduce(lambda a,b: a+b, filter(lambda x: x%2==0, nums)))  # 12

# 18. Count Words with Length Greater Than 3
words = ["cat", "apple", "dog", "banana"]
print(len(list(filter(lambda x: len(x)>3, words))))  # 2

# 19. Sum of Squares of Odd Numbers
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a,b: a+b, map(lambda x: x**2, filter(lambda x: x%2!=0, nums))))  # 35

# 20. Sum of Cubes of Even Numbers
nums = [1, 2, 3, 4, 5, 6]
print(reduce(lambda a,b: a+b, map(lambda x: x**3, filter(lambda x: x%2==0, nums))))  # 288
