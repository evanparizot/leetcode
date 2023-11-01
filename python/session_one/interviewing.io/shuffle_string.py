# 1) Write a function that takes a string as an input and returns a shuffled version of that string 
# (i.e. a version where each character is just as likely to be in any given position)

# 2) Write a function that analyzes how well your previous function randomly shuffles the string

import random
def shuffle(word: str) -> str:
  indices = list(range(0, len(word)))
  letters = list(word)

  while len(indices) > 1:
    x = indices.pop(random.randrange(len(indices)))
    y = indices.pop(random.randrange(len(indices)))
    letters[x], letters[y] = letters[y], letters[x]

  return "".join(letters)


# def evaluate(original: str, shuffled: str):
  


print(shuffle("My string"))