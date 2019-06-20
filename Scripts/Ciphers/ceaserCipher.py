#Ceaser Cipher - Simple Python Cipher Script
#Thomas S
#30 May 2019
#

#Start of program
#set a variable to hold alphabet and other numeric characters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#key to shif alphabet by
key = 13
encryptedmsg = ''

#Ask users if they want to encrypt or decrypt
answer = input('Would you like to encrypt of decrypt a message(Enter e to encrypt, d to decrypt):')

#if user wants to encrypt
if answer == 'e':

 message = input("Enter a message to encrypt using the ceaser cipher: ")

 for letter in message:

  index = ALPHABET.find(letter)

  #add key to the current letter
  index += key


  #if index wraps around
  if index > len(ALPHABET):
   index -= len(ALPHABET)

  encryptedmsg += ALPHABET[index]

 print("Your message encrypted is: " + encryptedmsg)

#if user wants to decrypt
else:

 message = input("Enter a message to decrypt using the ceaser cipher: ")


 for letter in message:

  index = ALPHABET.find(letter)

  index -= key

  if index < 0:
   index += len(ALPHABET)

  encryptedmsg += ALPHABET[index]


 print("Your message decrypted is: " + encryptedmsg)

