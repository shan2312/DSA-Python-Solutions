import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

from collections import Counter
def min_length_substring(s, t):
  t_hashmap = Counter(t)
  window_start = 0
  
  while window_start < len(s):
    if s[window_start] in t_hashmap:
      break
    window_start += 1
  
  for window_end in range(window_start, len(s)):
    letter = s[window_end]
     
    if letter in t_hashmap:
      t_hashmap[letter] -= 1
      if t_hashmap[letter] == 0: del t_hashmap[letter]
        
    if len(t_hashmap) == 0:
      return (window_end - window_start + 1)
        
        
  return -1
        
    
  
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  