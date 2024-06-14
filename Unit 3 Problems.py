# Unit 3, Session 1 Problems
# Problem 1: Calling Mississippi
def count_mississippi(limit):
  for num in range(1, limit):
  print( f"{num} mississippi")

# Problem 2: Swap Ends
def swap_ends(my_str):
  return  my_str[len(my_str)-1] + my_str[1:len(my_str)-1] + my_str[0]
my_str = "string"
swapped = swap_ends(my_str)
print(swapped)

# Problem 3: Pangrams
def is_pangram(my_str):
  hold = []
  for letter in my_str:
    if letter.lower() not in hold and letter.isalpha():
      hold.append(letter.lower())
  if len(hold) == 26:
    return True
  return False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# Problem 4: Reverse String
def reverse_string(my_str):
  hold = ''
  for idx, elem in enumerate(my_str):
    hold += my_str[(len(my_str) -1) - idx]
  return hold

my_str = "live"
print(reverse_string(my_str))

my_str = "frank"
print(reverse_string(my_str))

# Problem 5: 1st Unique Char
def first_unique_char(my_str):
  for n in range(len(my_str)):
    val = my_str.count(my_str[n])
    if(val==1):
      return n
  return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

# Problem 6: Minimum Distance
"""
def min_distance(words,word1,word2):
  dict = {}
  distances = []
  for idx, word in enumerate(words):
"""
def min_distance(words, word1, word2):
  word1in = []
  word2in = []
  distances = []
  for n in range(len(words)):
    if (words[n] == word1):
      word1in.append(n)
    if (words[n] == word2):
      word2in.append(n)
  for n in word1in:
    for x in word2in:
      distances.append(abs(n - x))
  return min(distances)

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

# Problem Set B, Problem 2: Remove Char
def remove_char(s, n):
  return s[0:n] + s[n+1:len(s)]
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
