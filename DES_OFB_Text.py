def pad(text):
    while len(text)%8!=0:
        text+=' '
        
    return text
	
	

from Crypto.Cipher import DES

from Crypto import Random

iv = Random.get_random_bytes(8)

des1 = DES.new(b'01234567', DES.MODE_OFB, iv)

des2 = DES.new(b'01234567', DES.MODE_OFB, iv)

text = 'Real faces are the new secrets'
text=pad(text)
text=str.encode(text)
cipher_text = des1.encrypt(text)

decipher_text=des2.decrypt(cipher_text)