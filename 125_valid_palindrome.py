class Solution():
  def isPalindrome(self, s: str) -> bool:
    if len(s) <= 1:
      return True
    chars = ''.join(c.lower() for c in s if c.isalpha())
    lchars = list(chars)
    i, j = 0, len(lchars)-1

    while i < j:
      if lchars[i] != lchars[j]:
        return False
      i += 1
      j -= 1
    return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))