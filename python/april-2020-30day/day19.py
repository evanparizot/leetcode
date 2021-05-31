from typing import List
class Solution():
  def search(self, nums: List[int], target:int) -> int:
    if nums is None or len(nums) == 0:
      return -1

    if len(nums) == 1:
      return 0 if nums[0] == target else -1

    # Find pivot
    left, right = 0, len(nums)-1
    while left < right:
      mid = (left + right) // 2
      if nums[mid] > nums[right]: left = mid + 1
      else: right = mid
    
    print(left)
    # Then do binary search
    pivot = left
    left, right = 0, len(nums)-1

    if target >= nums[pivot] and target <= nums[right]:
      left = pivot
    else:
      right = pivot

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
          return mid
        else:
          if target < nums[mid]:
            right  = mid - 1
          else:
            left = mid + 1
    return -1




s = Solution()
print(s.search([5,1,3],5))
# print(s.search([3,1],0))
# print(s.search([1,3], 0))
# print(s.search([4,5,6,7,0,1,2], 3))
# print(s.search([4,5,6,7,8,9,0,1,2,3], 5))