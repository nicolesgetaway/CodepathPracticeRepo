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

# Session 2 Problems
# Problem 1: Sum of Strings
def sum_of_number_strings(nums):
  sum = 0
  for num in nums:
    sum += int(num)
  return sum
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)    # Expected: 60 (as an int, not str -> '60')

# Problem 2: Remove Duplicates
def remove_duplicates(nums):
  seen = []
  [seen.append(x) for x in nums if x not in seen]
  print (seen)
nums = [1,1,1,2,3,4,4,5,6,6]
remove_duplicates(nums)    # Expected: [1, 2, 3, 4, 5, 6]

# Problem 3: Reverse Letters Only
def reverse_only_letters(s):
#   hold = ''
#   """
#   for idx in range(len(s)):
#     if not s[idx].isalpha():
#       hold += s[idx] + s[(len(s)-1) - idx]
#     else:
#       hold += s[(len(s)-1) - idx]
#   return hold"""
#   idxDash = []
#   for i, elem in enumerate(s):
#     if elem == '-':
#       idxDash.append(i)
#   print(idxDash)
#   for i in range(len(s)):
#     if i in idxDash:
#       hold += '-'
#     else:
#       hold += s[(len(s)-1) - i]
#   return hold
# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# Need to draw a diagram for this one, like a insertion sort...
  hold = ''
  idxDash = []
  s_modified = ""
  for i, elem in enumerate(s):
    if elem == '-':
      idxDash.append(i)
    else:
      s_modified += elem
  print(idxDash)
  print(s_modified)
  i = len(s_modified)-1
  dash_index = 0
  while i >= 0:
    print("index", i)
    if dash_index in idxDash:
      hold += '-'
      idxDash.remove(dash_index)
      print(idxDash)
      # remove that index from idxDash
    else:
      hold += s_modified[i]
      i -= 1
    dash_index += 1
  return hold

def reverse_str(str):
  return str[::-1]
str = "abcdefg"
print(reverse_str(str))


# # Session 2 (Breakout Room Group Work)
# I already solved the first 3 problems so commented the additional solutions
# # Problem 1
# # U: Get strings that are integers and return the sum of those integers

# # P: Create sum variable, iterate over the list, and convert the strings to integers and add them to the sum variable

# # def sum_of_number_strings(nums):
# #   sum = 0
# #   for num in nums:
# #     sum += int(num)

# #   return sum

# # nums = ["10", "20", "30"]
# # sum = sum_of_number_strings(nums)
# # print(sum)

# def remove_duplicates(nums):
#   # encounter first occurence of element
#   # save element
#   # sequentially move through list until element no longer matches first occurence
#   # do this until end of the list is reached
#   index = 0
#   while index < len(nums):
#     curr_element = nums[index]
#     while index < len(nums) and nums[index] == curr_element:
#       index += 1
#       nums.remove(curr_element)
#       print("Removing", curr_element)
#     index += 1
#     print("Index (out of loop)", index)
#   return nums
# nums = [1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8]
# print(remove_duplicates(nums))

# def reverse_only_letters(s):
#   hold = ''
#   idxDash = []
#   s_modified = ""
#   for i, elem in enumerate(s):
#     if elem == '-':
#       idxDash.append(i)
#     else:
#       s_modified += elem
#   print(idxDash)
#   print(s_modified)
#   i = len(s_modified)-1
#   dash_index = 0

#   while i >= 0:
#     print("index", i)
#     if dash_index in idxDash:
#       hold += '-'
#       idxDash.remove(dash_index)
#       print(idxDash)
#       # remove that index from idxDash
#     else:
#       hold += s_modified[i]
#       i -= 1
#     dash_index += 1
    
#   return hold
# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s) # j-Ih-gfE-dCba

def longest_uniform_substring(s):
  max_length = 1
  index = 0
  while index < len(s) - 1:
    current_length = 1
    while index < len(s) - 1 and s[index] == s[index+1]:
      index += 1
      current_length += 1
    if current_length > max_length:
      max_length = current_length
    index+= 1
  return max_length

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)