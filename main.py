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
"""
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
"""

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



