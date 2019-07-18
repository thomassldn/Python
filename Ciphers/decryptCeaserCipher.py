#Ceaser Cipher - Simple Python Cipher Script
#Thomas S
#30 May 2019
#

#Start of program
#set a variable to hold alphabet and other numeric characters
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#key to shif alphabet by
key = 0
decryptedMsg = ''

message = input("Enter a message to decrypt using the ceaser cipher: ")

for key in range(len(ALPHABET)):
   decryptedMsg = ''

   for letter in message:

    index = ALPHABET.find(letter)

    index -= key

    if index < 0:
     index += len(ALPHABET)

    decryptedMsg += ALPHABET[index]

   print('Key #%s: %s' % (key, decryptedMsg))


