
"""
### Install the library for Anaconda

pip install des

conda install -c conda-forge pycryptodome  
"""


from des import DesKey
key0=DesKey(b"some key")  #All keys should be BYTES form

msg=b"LIFE IS ALL ABOUT CHALLENGES"

print(msg)

encrypted_msg=key0.encrypt(msg,padding=True) #padding=True => Message becomes multiple of 8
print(encrypted_msg)


decrypted_msg=key0.decrypt(encrypted_msg,padding=True)
print(decrypted_msg)