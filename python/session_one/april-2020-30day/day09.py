# Given two strings S and T, return if they are equal when both are typed into 
# empty text editors. # means a backspace character

# Ex
# Input: S = "ab#c", T = "ad#c"
# Output: True
# Both S and T become "ac"

# Can you solve this in O(n) time and O(1) space?

from typing import List
def backspaceCompare(S: str, T: str) -> bool:
  # One way could be to iterate through string's characters
  # If we encounter a backspace character, attempt to delete previous char (if it exists)

  def removeChars(chars: List[chr]):
    i = 0
    while i < len(chars): 
      if chars[i] == '#':
        # If it's a backspace character, need to remove it and the char before it
        if i != 0:
          del chars[i]
          del chars[i-1]
          i -= 1
        else:
          del chars[i]
      else:
        i += 1
    return chars
  
  return "".join(removeChars(list(S))) == "".join(removeChars(list(T)))






print(backspaceCompare("ab#c","ad#c")) # True
print(backspaceCompare("a##c","#a#c")) # True
print(backspaceCompare("a#c","b")) # False