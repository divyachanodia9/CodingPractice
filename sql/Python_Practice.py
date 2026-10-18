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


## Arrays and Hashing
# 1) Two Sum :

class Solution:
    def two_sum(nums,target):
        hash_map = {}

        for i in range(len(nums)):
            k = target - hash_map[nums[i]]
            if k in hash_map:
                return [hash_map[k], i]
            else:
                hash_map[nums[i]] = 1

# 2) Valid Anagram: TC - O(n + n) ~ O(2n), SC: O(26)
class Solution:
    def isAnagram(s,t):
        if len(s) != len(t):
            return False

        d = {}

        for ch in s:
            d[ch] = d.get(ch,0) + 1
        for ch in t:
            if ch not in d:
                return False
            if d[ch] == 0:
                return False
            d[ch] -= 1
        return True

# 3) Group Anagram 
# input : strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:
    def grpAnagrams(strs):
        d = defaultdict(list)
        for word in words:
            sorted_word = "".json(sorted(word))
            d[sorted_word].append(word)
        return list(d.values())

# 4) Top K frequent Elements
# input : [1,2,1,2,1,2,3,1,3,2], k = 2
class Solution:
    def topKfrequent(nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    maxi = float('-inf')
    new_freq = {}
    for k,v in freq.items():
        maxi = max(maxi,v)
        if v not in new_freq:
            new_freq[v] = [k]
        else:
            new_freq[v].append(k)        

    i = maxi
    output =[]
    while i > 0:
        if i in new_freq:
            output.extend(new_freq[i])
            if len(output) == k:
                return output
        i -= 1


# 5) Product of Array Except Self
# input : nums = [-1,1,0,-3,3]
class Solution:
    def productExceptSelf(nums):
        ls = [1] * len(nums) 
        rs = [1] * len(nums)
        f = [1] * len(nums)

        for i in range(1,len(nums)):
            ls[i] = ls[i-1] * nums[i-1]

        for j in range(len(nums)-2,-1,-1):
            rs[j] = rs[j+1] * nums[j+1]

        for k in range(len(nums)):
            f[k] = ls[k] * rs[k]

        return f