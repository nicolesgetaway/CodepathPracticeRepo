# Unit 4 Problems
# Session 1
def first_palindrome(words):
  for s in words:
    if s == s[::-1]:
      return s
  return ""
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
def remove_duplicates(nums):
  pointer1 = 0
  pointer2 = 1
  while pointer2 < len(nums):
    if nums[pointer1] == nums[pointer2]:
      nums.remove(nums[pointer1])
      print(nums)
    else:
      pointer1 += 1
      pointer2 += 1
  return nums
nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list

# Session 2
def is_long_pressed(name, typed):
  i, j = 0, 0  # Pointers for name and typed

  while j < len(typed):
      if i < len(name) and name[i] == typed[j]:
          # If characters match, move both pointers
          i += 1
      elif j == 0 or typed[j] != typed[j - 1]:
          # If characters don't match and it's not a long press scenario
          return False
      # Move the pointer for typed string
      j += 1

  # Check if all characters in name have been matched
  return i == len(name)

# Example usage
name1 = "alex"
typed1 = "aaleex"
print(is_long_pressed(name1, typed1))  # True

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))  # False

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))  # True

def find_content_children(g,s):
  contentChildren = 0
  s = sorted(s)
  g = sorted(g)
  pointerKid = len(s) - 1
  pointerCookie = len(g) - 1
  while pointerKid >= 0 and pointerCookie >= 0:
    if s[pointerCookie] >= g[pointerKid]:
      contentChildren += 1
      pointerCookie -= 1
    pointerKid -= 1

  return contentChildren
g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child
# Output: 2

# Example 2:
g = [2, 1]
s = [1,1,2]
# tip: sort both lists in order to make pointer incrementation easier
g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

find_content_children(s, g) 
# Output: 2 