# Unit 1, Session 2, Problem Set 1
# Problem 5: Max Difference
def max_difference(lst):
  a = max(lst)
  b = min(lst)
  return a-b
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

# Problem 6: Beyond Threshold
def count_less_than(numbers, threshold):
  counter = 0
  for i in numbers:
    if i < threshold:
      counter += 1
  return counter
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

# Problem 7: Get Evens
def get_evens(lst):
  a = []
  for i in lst:
    if i%2==0:
      a.append(i)
  return a
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

# Problem 8: Multiples of Five
def multiples_of_five():
  for i in range(0, 101, 5):
    print(i)
multiples_of_five()

# Unit 2, Session 1, Problem Set A
# Problem 1: Subsequences
# This solution finds subsequences, but doesn't maintain relative order
def is_subsequence(lst, sequence):
  a = []
  for i in lst:
    for j in sequence:
      if i == j:
        [a.append(i) for i in sequence if i not in a] # prevents duplicates returning as True
  if a == sequence:
    return "True"
  else:
    return "False"
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, -1, 6, 10] # should be False, returns True
print(is_subsequence(lst, sequence))

# Corrected solution that satisfies all tests cases (duplicates and out-of-order)
def is_subsequence(lst, sequence):
  x = 0
  y = 0
  while x < len(sequence) and y < len(lst):
    if sequence[x] == lst[y]:
      x += 1
    y += 1
    if y == len(lst) and x != len(sequence):
      return False
  return True
lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, -1, 6, 10] # False
# sequence = [1, 6, 6, 10] # False
sequence = [1, 6, -1, 10] # True
print(is_subsequence(lst, sequence))

# Problem 2: Create Dictionary
def create_dictionary(keys, values):
  d = {}
  for i in range(len(keys)):
    d[keys[i]] = values[i]
  return d
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))

# Problem 3: Print Pair
def print_pair(dictionary, target):
  if dictionary.get(target) is not None :
    print("Key: " + target + "\nValue: " + dictionary.get(target))
  else:
    print("That pair does not exist!")
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "squidward")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

# Problem 4: Keys Versus Values
def keys_v_values(dictionary):
  sK = sum(dictionary.keys())
  sV = sum(dictionary.values())
  if sK > sV:
    return "keys"
  elif sK < sV:
    return "values"
  else:
    return "balanced"
dictionary1 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)


# Problem 5: Restock Inventory
def restock_inventory(current_inventory, restock_list):
  for key, value in restock_list.items():
    current_inventory[key] = value
  return current_inventory
current_inventory = {
  "apples": 30,
  "bananas": 15,
  "oranges": 10
}

restock_list = {
  "oranges": 20,
  "apples": 10,
  "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# Problem 6: Calculate GPA
def calculate_gpa(report_card):
  gpa = 0.00
  letterGrades = {"A": 4.00, "B": 3.00, "C": 2.00, "D":1.00, "F":0.00}
  for i in report_card.values():
    gpa += float(letterGrades.get(i))
  return gpa/len(report_card)
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

# Problem 7: Highest Rated
def highest_rated(books):
  a = []
  highest = {}
  for book_dict in books:
      for key, val in book_dict.items():
        if key == 'rating':
          a.append(val)
      if book_dict.get("rating") == max(a):
        highest = book_dict
  return highest
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books)) 

# Problem 8: Index-Value Map
def index_to_value_map(lst):
  d = {}
  for i in range(len(lst)):
    d[i] = lst[i]
  return d
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

# Unit 2, Session 2, Problem Set A
# Problem 1: Cast Vote
def cast_vote(votes, candidate):
  if votes.get(candidate) is None:
    votes[candidate] = 0      #added unregistered candidate to dict
  for key, value in votes.items():
    if key == candidate:
      votes[candidate] = value + 1      #updates vote for desired candidate
  return votes
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

# Problem 2: Common Keys
def common_keys(dict1, dict2):
  a = []
  for k in dict1:
    if dict2.get(k) is not None:
      a.append(k)
  return a
# Test 1 (Example Input Given)
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
# Test 2
dict1 = {"a": 1, "b": 2, "c": 3, "d":1}
dict2 = {"b": 4, "d": 5, "a": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# Problem 3: Get Highest Priority
def get_highest_priority_task(tasks):
  highest = max(tasks.values())
  priority = []
  for key in tasks:
    if tasks.get(key) == highest:
      priority.append(key)
  tasks.pop(priority[0])
  return priority[0]  

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}

perform_task = (get_highest_priority_task(tasks)) # removes task2 bc first in alphabet
print(perform_task)
perform_task = (get_highest_priority_task(tasks)) # removes task4
print(perform_task)
perform_task = (get_highest_priority_task(tasks)) # removes task3
print(perform_task)
print(tasks) # task1, task5 should be left

# Problem 4: Count Occurrences (Frequency Map)
def count_occurrence(nums):
  a = {}
  for num in nums:
    if num in a:  # frequency counter
      a[num] += 1
    else:   # creates new entry, prevents KeyError
      a[num] = 1
  return a

#nums = [1, 2, 2, 3, 3, 3, 4]
#print(count_occurrence(nums))
# Problem 5: Majority Element (uses function from Problem 4)
def find_majority_element(elements):
  freq = count_occurrence(elements)
  i = len(elements)
  for key in freq:
    if freq[key] > i/2:
      return key
    else:
      return None
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))  # should print '2'
elements = [1, 1, 1, 1, 1, 2, 2]
print(find_majority_element(elements)) # should print '1'
elements = [1, 1, 1, 2, 2, 2]
print(find_majority_element(elements)) #should print None

# Problem 6: Find duplicates
def hasDuplicates(nums, k):
  if k > len(nums):
    k = len(nums)
  seen = []
  for i in range(k):
    #print(nums[i])
    if nums[i] in seen:
      return True
    else:
      seen.append(nums[i])
  return False
nums = [5, 6, 8, 2, 4, 6, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 4)
print(check2)
check3 = hasDuplicates(nums, 9)
print(check3)

# Problem 7: Make Pairs (uses Problem 4 function)
def divideList(nums):
  freq = count_occurrence(nums)
  allEven = True
  canDivide = None
  for value in freq.values():
    if value %2 != 0:
      allEven = False
  canDivide = bool(len(nums)%2 == 0 and allEven)
  print(canDivide)
nums = [3,2,3,2,2,2]
divideList(nums) # should be True, pairs: (2,2) (2,2) (3,3)
nums = [1,2,3,4]
divideList(nums) # should be False
nums = [5,6,5,6,5,6]
divideList(nums) # should be False, uneven frequency
nums = [6,5,6,5,6,5,5,6]
divideList(nums) # should be True, pairs: (5,5) (5,5) (6,6) (6,6)