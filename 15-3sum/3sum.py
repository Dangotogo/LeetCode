# class Solution(object):
#     def threeSum(self, nums):
       
        
#         nums = sorted(nums)
#         result = []

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(len(nums)-1):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append([nums[i], nums[j], nums[k]])
#                     elif nums[i] + nums[j] + nums[k] > 0:
#                         k -= 1
#                     else:
#                         i += 1
#                         j += 1

        
#         return result

    
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Sorted: if the smallest number is positive, no triplet can sum to 0
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1          # need a bigger sum
                elif total > 0:
                    right -= 1         # need a smaller sum
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates on the left side
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

# For each element at index i:
#   1. Skip duplicates of this element
#   2. Set left = i + 1, right = last_index
#   3. While left < right:
#      - Calculate current_sum = nums[i] + nums[left] + nums[right]
#      - If sum == 0: add to result, move both pointers
#      - If sum < 0: increment left pointer
#      - If sum > 0: decrement right pointer
