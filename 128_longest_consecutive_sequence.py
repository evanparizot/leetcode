from typing import List
def longestConsecutive(nums: List[int]) -> int:
  best = 0
  x = {i: 1 for i in nums}

  for i in list(x.keys()):
    if i not in x:
      continue
    counter = 1
    j = 1
    while i + j in x:
      counter += 1
      del x[i + j]
      j += 1
    
    j = 1 # reset j
    while i - j in x:
      counter += 1
      del x[i-j]
      j += 1
    
    del x[i]
    best = max(best, counter)
    if not x:
      break
  return best


longestConsecutive([1,2,3,99,4,5,100,101])