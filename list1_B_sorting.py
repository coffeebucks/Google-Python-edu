# tested: sort methods with key functions/functions/combine list/for loop.

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

sentence = ['iron man', 'deadpool', 'x man', 'xtra power juice']
def front_x(words):
  newList1 = []
  newList2 = []
  for word in words:
      if word.startswith('x'):
          newList1.append(word)
      else:
          newList2.append(word)
  return sorted(newList1) + sorted(newList2)
print(front_x(sentence))
