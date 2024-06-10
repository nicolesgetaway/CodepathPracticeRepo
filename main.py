"""
def max_difference(lst):
  a = max(lst)
  b = min(lst)
  return a-b
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

def count_less_than(numbers, threshold):
  counter = 0
  for i in numbers:
    if i < threshold:
      counter += 1
  return counter
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

def get_evens(lst):
  a = []
  for i in lst:
    if i%2==0:
      a.append(i)
  return a
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

"""

def multiples_of_five():
  for i in range(0, 101, 5):
    print(i)
multiples_of_five()
