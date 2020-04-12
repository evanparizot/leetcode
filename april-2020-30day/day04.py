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


# Solution 3:
# Without needing any additional space, can:
# 1. Iterate through array with two pointers
# 2. Increment slow when encountering a non-zero
# 3. Increment fast everytime


from typing import List

class Solution():
  def moveZeroes(self, nums: List[int]) -> None:
    # Solution 2:
    # i = 0
    # length = len(nums)
    # while(i < length):
    #   if nums[i] == 0:
    #     nums.pop(i)
    #     nums.append(0)
    #     length -= 1
    #   else:
    #     i += 1

    # Solution 3:
    # slow, fast = 0, 0
    # while fast < len(nums):
    #   if nums[slow] == 0 and nums[fast] != 0:
    #     nums[slow], nums[fast] = nums[fast], nums[slow]

    #   if nums[slow] != 0:
    #     slow += 1
    #   fast += 1

    # Solution 4:
    length = len(nums)
    nums[:] = [num for num in nums if num != 0] 
    # https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
    # https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps

    # Reference on list[:] or string[:]
    # https://realpython.com/python-lists-tuples/

    nums += [0]*(length-len(nums))


def main():
  s = Solution()
  a = [1,4,0,2,4,0,0,1]
  s.moveZeroes(a)
  print(a)

if __name__ == "__main__":
  main()