"""
# install gmpy2
 #  conda install -c conda-forge gmpy2

"""

from Crypto.Util.number import *
from Crypto import Random
import Crypto
import gmpy2
import sys


#no of bits for random number 
bits=60
msg="Codemonks"

# Generate the random no with 60 bits

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

n = p*q
PHI=(p-1)*(q-1)
print("PHI: ",PHI)

#65537 is  possible prime no 
e=65537

# Find modular inverse of e under PHI
d=(gmpy2.invert(e, PHI))

m=  bytes_to_long(msg.encode('utf-8'))

c=pow(m,e, n)
res=pow(c,d ,n)
print("Result: ",res)
print ("Message=%s\np=%s\nq=%s\nN=%s\ncipher=%s\ndecipher=%s" % (msg,p,q,n,c,(long_to_bytes(res))))