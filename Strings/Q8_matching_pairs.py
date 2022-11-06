import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

import collections

def matching_pairs(s, t):
  swap = False

  s = list(s)
  t = list(t)
  
  letter_to_index_s = collections.defaultdict(list)
  letter_to_index_t = collections.defaultdict(list)
  
  for i in range(len(s)):
    letter_to_index_s[s[i]].append(i)
    letter_to_index_t[t[i]].append(i)
  
  match = 0
  for i in range(len(s)):
    if s[i] == t[i]:
      match += 1
      continue
    else:
      if s[i] in letter_to_index_t:
        indexes_t = letter_to_index_t[s[i]]
        
        for index in indexes_t:
          if s[index] == t[i]:
            s[index], s[i] = s[i], s[index]
            
        if s[i] != t[i]:
          s[i], s[indexes_t[0]] = s[indexes_t[0]], s[i]
        swap =True
          
        match += 1

  if not swap and match == len(s):
      return len(s) - 2
      
  if not swap and match != len(s):
      return len(s)
        
        
  return match


def matching_pairs1(s, t):
    if not s or not t:
      return

    match_count = 0
    duplicate = set()
    s_left = []
    t_left = []
    for x, y in zip(s, t):

      if x == y:
        match_count += 1
        duplicate.add(x)
      
      else:
        s_left.append(x)
        t_left.append(y)
    
    s_in_t = 0
    t_left = set(t_left)
    for char in s_left:
      if char in t_left:
        s_in_t += 1
    
    if len(s_left) >= 2:

      return match_count + 1 if s_in_t == 1 else match_count + 2
    
    elif len(s_left) == 1:
      return match_count - 1 if len(duplicate) == match_count else match_count
    
    else:
      return match_count
            
            
        
      
      
  
  











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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  s_2, t_2 = "abcdl", "adcbb"
  expected_2 = 4
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  s_2, t_2 = "mlop", "nkjd"
  expected_2 = 4
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  s_2, t_2 = "aaa", "aaa"
  expected_2 = 3
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  