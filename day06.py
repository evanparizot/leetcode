from typing import List
from collections import defaultdict
# give an array of strings, group anagrams together

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  # O(n^2)
  anagrams = defaultdict(list)
  for word in strs:
    anagrams[''.join(sorted(word))].append(word)
  return list(anagrams.values())

if __name__ == "__main__":
  print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))