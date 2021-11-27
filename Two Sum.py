def twosum(nums, target):
    lookup = {}
    for cnt, num in enumerate(nums):
        if target - num in lookup:
            return lookup[target-num], cnt
        lookup[num] = cnt 
        
print(twosum([1,8,5,3],4))
