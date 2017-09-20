# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
  return
  
  
def match_ends(words):
    count = 0
    for word in words:
        if len(words) >= 2 and word[0] == word [-1]:
            count += 1
    return count
match_ends(string)    
