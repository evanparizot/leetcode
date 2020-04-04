# Move Zeroes
# Give an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements
# Must do this in-place (can't copy the array)
# Minimize the total number of operations


# Notes

# Solution 1:
# If we were allowed to use an additional array, could:
# 1. Initialize an empty array
# 2. Iterate through given array and pop 0's out of list and put in other list
# 3. Then append zero list to original list

# Solution 2:
# Without using an additional array, can:
# 1. Iterate through array
# 2. When encountering a zero, pop and append to end of list
# 3. Decrease total length
# 4. If not a zero, just increase index


from typing import List

class Solution():
  def moveZeroes(self, nums: List[int]) -> None:
    # Solution 2:
    i = 0
    length = len(nums)
    while(i < length):
      if nums[i] == 0:
        nums.pop(i)
        nums.append(0)
        length -= 1
      else:
        i += 1

def main():
  s = Solution()
  a = [1,4,0,2,4,0,0,1]
  s.moveZeroes(a)
  print(a)

if __name__ == "__main__":
  main()