#Sha-256 hash algorthim
#Thomas S
#21 June 2021

import hashlib

def encode(message):

    encoded = hashlib.sha256(message.encode())
    
    return encoded

#Get users message
message = input("Enter string: ")
print ("Message: ", message)

#Encode Users Message and print it
encoded_message = encode(message)
print("Encoded: ", encoded_message)

#Print the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(encoded_message.hexdigest())
