### this is not the algorithm!
### plus, not very efficient.

nums=[i for i in range(4,150)]
#remove all none prime numbers in nums
for i in range(2,150):
    for j in range(2,150):
        if i*j in nums:
            nums.remove(i*j)
print(nums)
