from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  text_list = list(start_text)
  caesar_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in text_list:
    # If the user enters any characters that are non letters i.e numbers, spaces or symbols,
    # these characters will not be shifted and thus will be left in place
    if char in alphabet:
      index = alphabet.index(char)
      shifted_index = index + shift_amount
      if shifted_index > (len(alphabet) - 1):
        index = alphabet.index(char) - len(alphabet)
        shifted_index = index + shift_amount
        caesar_text += alphabet[shifted_index]
      else:
        caesar_text += alphabet[shifted_index]
    # Spaces, symbols, or numbers will be left in place while letters are shifted
    else: 
      caesar_text += char
  print(f"Here is the encoded result: {caesar_text}\n")

# If a user wants to continue encoding messages, this section will either continue the program,
# or end it depending on the user's input 
program_on = True

while program_on:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
#   If a user enters a number that is larger than the length of the alphabet, this
#   section will duplicate the alphabet according to the user's shift input amount such that
#   the index of the letter in the new alphabet corresponds to the shift amount
  # My solution:
  if shift > len(alphabet):
    alphabet_multiplier = int(shift / len(alphabet))
    if alphabet_multiplier > 0:
      alphabet *= alphabet_multiplier + 1
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart_program = input("Type 'yes' if you ant to go again. Otherwide, type 'no'\n")

  if restart_program == "no":
    print("Good Bye")
    program_on = False
  elif restart_program == "yes":
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)