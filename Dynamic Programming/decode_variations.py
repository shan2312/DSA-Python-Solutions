def is_valid(s):
    s_int = int(s)

    return s_int > 0 and s_int < 27 and len(s) == len(str(s_int))

def get_variations(s):
    pointer1, pointer2 = 1, is_valid(s[0])

    for index in range(1, len(s)):
        pointer1, pointer2 = pointer2, (is_valid(s[index]) * pointer2 + is_valid(s[(index - 1): (index + 1)])*pointer1)

    return pointer2

def decode_variations_iterative(S):
  variations_list = [0] * (len(S) + 1)
  variations_list[-1] = 1
  
  
  for index in range(len(S) - 1, -1, -1):
    if is_valid(S[index]):
      variations_list[index] += variations_list[index + 1]
      
    if (index + 1) < len(S) and is_valid(S[index: (index + 2)]):
      variations_list[index] += variations_list[index + 2]
      
  return cache[0]


print(get_variations("122212313113"))