def gcd(a,b): 
    if b==0:
        return a 
    else:
        return gcd(b,a%b)

def encryptRSA(no, e, n):
    encrypted = pow(no, e) % n
    print('Cipher Text = '+ str(encrypted))
    return encrypted

# multipled by  e which will give remainder as 1 when modulo phi 
def decryptRSA(cipherdata, d, n):
    decrypted = pow(cipherdata, d) % n
    print('Decrypted Text = '+ str(decrypted))
    return decrypted

# sample input 
# Enter the value of p = 53
# Enter the value of q = 59
# Enter the value of text = 89

#Message M should always be in between 1 to N-1 to follow the Totient Theorem of Number theory

p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q

phi = (p-1)*(q-1)

print('n = ' + str(n))
print('phi = ' + str(phi))

#find e
e = 0
for ee in range(2,phi): 
    if gcd(ee,phi)== 1:
        print('Value of e (public key):' + str(ee))
        e = ee
        break
        
# find d     
for i in range(1,phi): 
    x = 1 + i*phi 
    if x % e == 0: 
        d = int(x/e)
        print("Value of x: ",x)
        print("Value of i: ",i)
        print('Value of d (private key):' + str(d))
        break
		
		
		
encrypted = encryptRSA(no, e, n)

decrypted = decryptRSA(encrypted, d, n)



def isPrime(n): 
    # Corner case 
    if n <= 1 : 
        return False
    # check from 2 to n-1 
    for i in range(2, n): 
        if n % i == 0: 
            return False
  
    return True

def getPrimes(n):
    lst = []
    for i in range(2, n + 1): 
        if isPrime(i): 
            lst.append(i)
    return lst

#Now in factorisation attack we get p and q which are prime and give product as n

def factorisationAttack(n, e, cipherdata):
    primes = getPrimes(n)
    p1 = 0
    q1 = 0
    d1 = 0
    for i in primes:
        for j in primes:
            if i!=j :
                temp = i*j
                if(temp == n):
                    p1 = i
                    q1 = j
                    break;
                
    if(p1 == 0 and q1 == 0):
        print('No p and q found')
        return
    else:
        print('Found p and q')
        print('p: '+ str(p1) +' q:' + str(q1))
        phi = (p1-1)*(q1-1)
        for i in range(1,phi): 
            x = 1 + i*phi 
            if x % e == 0: 
                d1 = int(x/e) 
                break
        decryptRSA(cipherdata, d1, n) 
        print('RSA broken successfully')

# sample input
# Enter the value of cipherdata = 1394
# Enter the value of n = 3127
# Enter the value of e = 3

cipherdata = int(input('Enter the value of cipherdata = ')) 
n = int(input('Enter the value of n = ')) 
e = int(input('Enter the value of e = ')) 

factorisationAttack(n, e, cipherdata)