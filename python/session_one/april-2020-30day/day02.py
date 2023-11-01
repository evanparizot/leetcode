
# https://leetcode.com/problems/happy-number/discuss/560153/Python-Space-O(1)-and-O(n)-Simple-Concise-Solutions
class Solution:
  # Python 3.8 version. Requires support for walrus (:=) operator

  # def isHappy(self, n: int) -> bool:
  #   visited = set()
  #   while (n:= sum(map(lambda x: int(x)**2, str(n)))) != 1 and not n in visited:
  #     visited.add(n)
  #   return not n in visited


  def isHappy(self, n: int) -> bool:
    visited = set()
    while n != 1 and not n in visited:        # if n is already in set, means we are stuck in loop
      visited.add(n)

      # sum(                                )       takes in iterable and adds all elements together
      #     map(                            )       takes in function and iterable. Applies function to every element in iterable.
      #         lambda x: int(x)**2                 for every input, raises to second power
      #                             , str(n)        casts numeral to string

      n = sum(map(lambda x: int(x)**2, str(n)))
    return not n in visited

def main():
  s = Solution()
  print(s.isHappy(100)) # True
  print(s.isHappy(19))  # True
  print(s.isHappy(2))   # False

if __name__ == "__main__":
  main()