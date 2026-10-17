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
# 1) Brute - Better Solution
num = n
result = []
for i in range(1,num//2):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

# TC : O(N/2) ~ O(N)
# SC : O(k) - k is the number of factor

# 2) Optimal Solution
from math import sqrt
num = n
result = []
for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num//i)
    result.sort()  ## TC: O(NlogN)
print(result)

# TC : O(sqrt(N)) + O(NlogN)
# SC : O(k)  - k is the number of factor 


## Frequency Map / Dictionary
nums = [5,6,7,7,7,1,111,1,3,9,1,1,3]

#Method 1:
freq_map = {}
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
# TC : O(N) - for loop
# SC : O(N)

#Method 2:
d = {}
n = len(nums)
for i in range(0,n):    
    d[nums[i]] = d.get(nums[i],0) + 1

# TC : O(N) - for loop
# SC : O(N)


## Leetcode : Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates()