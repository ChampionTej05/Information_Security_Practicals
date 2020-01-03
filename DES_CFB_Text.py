def pad(text):
    while len(text)%8!=0:
        text+=' '
        
    return text
	
	

from Crypto.Cipher import DES

from Crypto import Random

iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_CFB, iv)

des2 = DES.new(b'01234567', DES.MODE_CFB, iv)

text = 'Real faces are the new secrets'
print(text)
text=pad(text)
text=str.encode(text)

cipher_text = des1.encrypt(text)
print(cipher_text)

decipher_text=des2.decrypt(cipher_text)

print(decipher_text)