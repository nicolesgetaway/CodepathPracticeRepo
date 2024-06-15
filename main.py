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
  hold = ''
  """
  for idx in range(len(s)):
    if not s[idx].isalpha():
      hold += s[idx] + s[(len(s)-1) - idx]
    else:
      hold += s[(len(s)-1) - idx]
  return hold"""
  idxDash = []
  for i, elem in enumerate(s):
    if elem == '-':
      idxDash.append(i)
  print(idxDash)
  for i in range(len(s)):
    if i in idxDash:
      hold += '-'
    else:
      hold += s[(len(s)-1) - i]
  return hold
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
# Need to draw a diagram for this one, like a insertion sort...

    