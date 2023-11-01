# Given an integer arr, count element x such that x+1 is also in arr
# If there are duplicates in arr, count them seperately

from typing import List
def countElements(arr: List[int]) -> int:
  lookup = set(arr)
  result = 0
  for num in arr:
    if (num + 1) in lookup:
      result += 1

  return result

print(countElements([1,2,3])) # 2
print(countElements([1,1,3,3,5,5,7,7])) # 0
print(countElements([1,3,2,3,5,0])) # 3