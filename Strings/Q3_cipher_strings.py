FIRST_CHAR_UPPER_ASCII = ord('A')
FIRST_CHAR_LOWER_ASCII = ord('a')

FIRST_DIGIT_ASCII = ord('0')

def rotationalCipher(input_str, rotation_factor):
  ciphered_string = []
  
  for letter in input_str:
    
    if letter.isdigit():
      ciphered_string.append(chr(FIRST_DIGIT_ASCII + (ord(letter) + rotation_factor - FIRST_DIGIT_ASCII) % 10))
    elif letter.isalpha():
      if letter.isupper():
        ciphered_string.append(chr(FIRST_CHAR_UPPER_ASCII + (ord(letter) + rotation_factor - FIRST_CHAR_UPPER_ASCII) % 26))
      elif letter.islower():
        ciphered_string.append(chr(FIRST_CHAR_LOWER_ASCII + (ord(letter) + rotation_factor - FIRST_CHAR_LOWER_ASCII) % 26))
    else:
      ciphered_string.append(letter)
      
  return "".join(ciphered_string)


if __name__ == '__main__':
    print(rotationalCipher('1', 5))