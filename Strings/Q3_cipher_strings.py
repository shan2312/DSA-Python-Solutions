FIRST_CHAR_UPPER_ASCII = ord('A')
FIRST_CHAR_LOWER_ASCII = ord('a')

FIRST_DIGIT_ASCII = ord('0')

def rotationalCipher(input_str, rotation_factor):
  ciphered_string = []
  
  for letter in input_str:
    
    letter_code = ord(letter)

    if letter.isdigit():
      new_letter = get_new_letter(letter_code, rotation_factor, FIRST_DIGIT_ASCII, 10)

    elif letter.isalpha():
      
      if letter.isupper():
        new_letter = get_new_letter(letter_code, rotation_factor, FIRST_CHAR_UPPER_ASCII, 26)
      elif letter.islower():
        new_letter = get_new_letter(letter_code, rotation_factor, FIRST_CHAR_LOWER_ASCII, 26)

    else:
      new_letter = letter
      
    ciphered_string.append(new_letter)
      
  return "".join(ciphered_string)


def get_new_letter(letter_code, rotation_factor, start_letter_code, count_of_letters):

  new_letter_code = letter_code + rotation_factor
  new_letter_code = new_letter_code - start_letter_code
  
  return chr(start_letter_code + new_letter_code % count_of_letters)


if __name__ == '__main__':
    print(rotationalCipher('xyz', 5))