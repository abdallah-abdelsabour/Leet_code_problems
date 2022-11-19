# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

in enumerate(iterable)
#    O(n2) worst case 
def findsum_1(nums , target):
  for i in range(len(nums)):
      for l in range(i+1, len(nums)):
         if nums[l] + nums[i] ==target:
            return [i , l ]
  return None


def find_sum_2(nums,target):
  d={}
  for i in range(len(nums)):
    if target -nums[i] in d :
      return [d[target - nums[i]] , i]
    else:
      d[nums[i]] = i





res = findsum_1([3,3], 6)
res2 = find_sum_2([3,3], 6)

print(res)
print(res2)