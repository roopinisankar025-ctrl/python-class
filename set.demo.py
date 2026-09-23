'''m={10,20,50,40,80}
print(m)
m.add(30)
print(m)
m.update([70,60])
print(m)
m.remove(40)
print(m,"throw error")
m.discard(500)
print(m,"not throw error")
print(20 in m)

set1={1,2,3,4}
set2={1,2,5,6}

print(set1| set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)'''


#------task--------
'''set1=[2,4,3,1]
set2=[3,3,1,7]
n=set(set1)
print(type(n))
n=

print(set1.intersection (set2))'''

print("1------------------")

a = [1, 2, 2, 3, 4]
b = [2, 2, 4, 5]
s1 = set(a)
s2 = set(b)
print(s1 & s2)

print("2-------------------------------------")

sen = "Python is easy, and Python is useful."
sen = sen.replace(",", "").replace(".", "")
words = set(sen.split())
print(words)

print("3------------------------------------")

a = [1, 2, 3, 4]
even = [x for x in a if x % 2 == 0]
print(even)

print("4----------------------")

s = {1, 2}
subsets = [set(), {1}, {2}, {1, 2}]
print(subsets)

print("5--------------------")

a = {1, 2, 3}
b = {3, 1, 2}
print(a == b)

print("6--------------------")
a = {1, 2, 3, 4}
b = {2, 3, 4}
c = {2, 4, 5}
print(a & b & c)
print("7----------------------")
a = {1, 2, 3, 4}
b = {2, 3}
print(a - b)
print("8----------------------")

sets = [
    {1, 2, 3},
    {2, 3, 4},
    {2, 3, 5}
]
result = sets[0]
for s in sets:
    result = result & s
print(result)

print("9--------------")

s = {"a", "b", "a"}
word = "aba"
print(word == word[::-1])

print("10-----------")

s = {1, 2, 3}
count = 0
if sum(s) % 2 == 0:
    count = 1
print(count)

print("11-------------------")

a = [100, 4, 200, 1, 3, 2]
s = set(a)
longest = 0
for x in s:
    if x - 1 not in s:
        count = 1
        while x + count in s:
            count += 1
        longest = max(longest, count)
print(longest)

print("12--------------")

a = {1, 2, 3}
b = {2, 3, 4}
common = a & b
result = (a ^ b) - common
print(result)

print("13---------------")

s = {2, 4, 6, 8}
target = 10
for x in s:
    if target - x in s:
        print(x, target - x)
        break

print("14----------------")

a = {1, 2}
b = {1, 2, 3}
print(a < b)

print("15-------------------")

sets = [{1, 2, 3}, {2, 4}, {5, 6}]
result = set()
for s in sets:
    for x in s:
        if sum(x in other for other in sets) == 1:
            result.add(x)
print(result)

