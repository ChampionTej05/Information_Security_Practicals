alist1=[chr(ch+65) for ch in range(26)]
dict2={val: key for val, key in enumerate(alist1)}
dict1={key: val for val, key in enumerate(alist1)}

# Key modification if user given
# Remake the Key if short in length
def generate_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i] #concat message string if given key short in length
            i += 1
    return key
	
	
# Encryption Function
def encryptWithAutoKey(message, key_new):
    cipher_text = ''
    i = 0
    for letter in message:
        if letter == ' ':
            cipher_text += ' '
        else:
            x = (dict1[letter.upper()]+dict1[key_new[i].upper()]) % 26 #add both numbers and take modulo 26 
            i += 1
            cipher_text += dict2[x] # get character corresponding to the number
    return cipher_text 
	
	
# Decryption function
def decryptWithAutoKey(cipher_text, key_new):
    decrypt_txt = ''
    i = 0
    for letter in cipher_text:
        if letter == ' ':
            decrypt_txt += ' '
        else:
            x = (dict1[letter.upper()]-dict1[key_new[i].upper()]+26) % 26 #subtract both numbers and take modulo 26: opposite of encryption
            i += 1
            decrypt_txt += dict2[x] # get character 
    return decrypt_txt
	
	
	
message = input('Enter the text to be encrypted: ')
key = input('Enter the key: ')
key_new = generate_key(message, key)
print('Key:',key_new)
encrypted_text = encryptWithAutoKey(message, key_new)
decrypted_text = decryptWithAutoKey(encrypted_text, key_new)

print("Encrypted Text =", encrypted_text)

print("Decrypted Text =", decrypted_text)




################ USING RANDOM KEY ###################
# Main run of program
# message = 'ATTACK AT DAWN'
# key = 'SECRET'

import random, string

message = input('Enter the text to be encrypted: ')

#random generation of key of same length as message
key = ''.join(random.choice(string.ascii_uppercase) for x in range(len(message)))
print('Key:',key)

encrypted_text = encryptWithAutoKey(message, key)
decrypted_text = decryptWithAutoKey(encrypted_text, key)

print("Encrypted Text =", encrypted_text)
print("Decrypted Text =", decrypted_text)