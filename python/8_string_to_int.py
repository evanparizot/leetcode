class Solution():
  def myAtoi(self, string: str) -> int:
    chars = list(string.lstrip())
    for i, c in enumerate(list(chars)):
      if (c == '+' or c == '-'):
        if len(chars) <= 1 or not chars[i+1].isdigit():
          return 0
        continue
      elif not c.isdigit():
        chars = chars[0:i]
        break

    result = 0
    for i, c in enumerate(reversed(chars)):
      if c.isdigit():
        result += int(c) * (10 ** i)
      if c == "-":
        result *= -1
    maxi = (2 ** 31) -1
    mini = -2 ** 31
    
    if result > maxi:
      return maxi
    elif result < mini:
      return mini
    else:
      return result

s = Solution()
s.myAtoi("4193 with words")
s.myAtoi("    -42")