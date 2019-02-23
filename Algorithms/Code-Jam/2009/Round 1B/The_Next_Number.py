import itertools
import math

def calculate_permutations(n):
  perm = list(map("".join, itertools.permutations(n)))
  n = int(n)
  max = math.inf
  for order in perm:
    int_order = int(order)
    if int_order > n and int_order < max:
      max = int_order

  return max

q = int(input())
for _ in range(1, q + 1):
  n = int(input())

  next_permutation = str(calculate_permutations("0" + str(n)))
  next_permutation = next_permutation.lstrip("0")

  with open('The_Next_Number.txt', 'a') as the_file:
    the_file.write("Case #{}: {}\n".format(_, next_permutation))
