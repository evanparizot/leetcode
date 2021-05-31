def diffBetweenTwoStrings(source, target):
  """
  @param source: str
  @param target: str
  @return: str[]
  """

  # https://leetcode.com/problems/edit-distance/discuss/274951/Python-Classic-DP
  # https://www.youtube.com/watch?v=MiqoA-yF-0M

  # Find editing distance
  # dp(i, j) = the minimum number of edits required for the problem with strings source[i:] and target[j:]
  
  # if source[i] == target[j]
  #   dp(i,j) = dp(i+1, j+1)

  #   return 
  #memo = {}
  memo = [ [None for i in range(len(target))] for j in range(len(source))]

  def dp(i,j):
    if i == len(source) or j == len(target):
      return len(target)-j

    elif (i,j) not in memo:
      if source[i] == target[j]:
        memo[i][j] = dp(i+1, j+1)
      else:
        memo[i][j] = 1 + min(dp(i+1, j), dp(i, j+1)) # adding dp(i+1, j+1) covers cases for transformations
    return memo[i][j]
  
  # Use editing distance to construct answer
  ans = []
  i = 0
  j = 0

  while i < len(source) and j < len(target):
    if source[i] == target[j]:
      ans.append(source[i])
      i += 1
      j += 1
    else:
      # decide to subtract source[i] or add target[j]
      compare1 = dp(i+1, j)
      compare2 = dp(i, j+1)

      if compare1 <= compare2:
        ans.append("-" + source[i])
        i += 1
      else:
        ans.append("+" + target[j])
        j += 1

  while j < len(target):
    ans.append("+" + target[j])
    j+=1
  return ans

print(diffBetweenTwoStrings("CABAAABBC", "CBBC"))
print(diffBetweenTwoStrings("ABCDEFG","ABDFFGH"))