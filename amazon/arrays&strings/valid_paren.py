class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        if len(s) <= 1:
          return False

        for c in list(s):
          if c == '(' or c == '[' or c == '{':
            stack.append(c)
          else:
            if not len(stack):
              return False

            prev = stack.pop()
            if mapping[c] != prev:
              return False
        
        if len(stack):
          return False

        return True


s = Solution()
# print(s.isValid("()"))
# print(s.isValid('{[]}'))
print(s.isValid('([)]'))