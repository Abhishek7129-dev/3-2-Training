# 1. Fibonacci Series (n terms)
n = 10
a, b = 0, 1
print("Fibonacci Series:")
print(a, b, end=" ")
for i in range(n - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c

print("\n")

# 2. Check Prime Number
num = 29
flag = True

if num <= 1:
    flag = False

for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        flag = False
        break

if flag:
    print("Prime number")
else:
    print("Not a prime number")

print()

# 3. Reverse a String
s = "python"
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string:", rev)
print()

# 4. Count Vowels in a String
s = "education"
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowel count:", count)
print()

# 5. Sum of Digits of a Number
num = 1234
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)
print()

# 6. Armstrong Number
num = 153
temp = num
sum_arm = 0

while temp > 0:
    digit = temp % 10
    sum_arm += digit ** 3
    temp = temp // 10

if sum_arm == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

print()

# 7. GCD of Two Numbers
a = 48
b = 18

while b != 0:
    a, b = b, a % b

print("GCD =", a)
print()

# 8. Remove Duplicates from a List
lst = [1, 2, 3, 2, 4, 1, 5]
new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)
print()

# 9. Second Largest Number in a List
lst = [10, 20, 4, 45, 99]
largest = second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)
print()

# 10. Frequency of Characters in a String
s = "programming"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:", freq)