#String methods 

s = "hello"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
          #2

s = "hello "
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
       # 3

s = "hello "
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
         # 4
s = "HElloWorLd "
upper = 0
lower = 0
for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
            #5

s = "helloworld "
new = ""
for ch in s:
    if ch != " ":
        new += ch
print(new)
               #6

s = "apple "
for ch in s:
    count = 0
    for x in s:
        if ch == x:
            count += 1
    print(ch, count)
                  #7

s = "abc123 "
count = 0
for ch in s:
    if '0' <= ch <= '9':
        count += 1
print(count)
            #8

s = "hello"
yes = True
for ch in s:
    if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
        yes = False
if yes:
    print("Only alphabets")
else:
    print("Not only alphabets")
                 # 9

s = "hello "
new = ""
for ch in s:
    if 'a' <= ch <= 'z':
        ch = chr(ord(ch) - 32)
    new += ch
print(new)
                 #10

s = "hello "
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])
              #11

s ="helloworld "
count = 0
inside = False
for ch in s:
    if ch != " " and inside == False:
        count += 1
        inside = True
    elif ch == " ":
        inside = False
print(count)
               # 12
s = "apple "
new = ""
for ch in s:
    if ch in "aeiouAEIOU":
        new += "*"
    else:
        new += ch
print(new)
                   # 16

s = "good"
n = 2
for ch in s:
    for i in range(n):
        print(ch)
                 #15

s = "Hello Apple "
count = 1
for ch in s:
    if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9' or ch == " "):
        count += 1
print(count)
                     #17

s = "orange "
new = ""
for ch in s:
    if ch not in new:
        new += ch
print(new)
                    