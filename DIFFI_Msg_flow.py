
 
# Variables Used
sharedPrime = 23    # p
sharedBase = 5      # g
 
#Random varaibles Choosen by each party

maateSecret = 6     # a
BhagwanSecret = 15      # b
 
# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , sharedPrime )
print( "    Publicly Shared Base:  " , sharedBase )
 
# Maate Sends Bhagwan A = g^a mod p
A = (sharedBase**maateSecret) % sharedPrime
print( "\n  Maate Sends Over Public Chanel: " , A )
 
# Bhagwan Sends Maate B = g^b mod p
B = (sharedBase ** BhagwanSecret) % sharedPrime
print(" Bhagwan Sends Over Public Chanel: ", B )
 
print()

print( "Privately Calculated Shared Secret:" )
# Maate Computes Shared Secret: s = B^a mod p
maateSharedSecret = (B ** maateSecret) % sharedPrime
print( "    Maate Shared Secret: ", maateSharedSecret )
 
# Bhagwan Computes Shared Secret: s = A^b mod p
bhagwanSharedSecret = (A**BhagwanSecret) % sharedPrime
print( "    Bhagwan Shared Secret: ", bhagwanSharedSecret )