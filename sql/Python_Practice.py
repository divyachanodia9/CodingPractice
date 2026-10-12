## Extraction of digits - Count no. of digits, Reverse a Number, Check Palindrome, Amrstrong Number
n = 5873
num = n
c = 0
while n > 0:
    c += 1
    last_digit  = num % 10
    print(last_digit)
    num = num // 10

# TC : O(log 10(N))
# Sc : O(1)

## Check Palindrome
n = 1234
num = n
result = 0
while num > 0:
    ld = num % 10
    num = num // 10
    result = result * 10 + ld
print(if n == result)

# TC : O(log 10 (N))
# SC : O(2)

## Amrstrong Number : 153 = 1^3 + 5^3 + 3^3 = 153 (3 - no. of digits)
n = 153
num = n
total = 0
nod = len(str(n))

while num > 0:
    ld = num % 10
    total += (ld ** nod)
    num = num // 10
print(if total == n)

# TC : O(log 10 N)
# SC : O(1)

## Print all factors of a Given Number 10 - [1,2,5,10]

