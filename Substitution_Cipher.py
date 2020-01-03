import random

msg="shift cipher is simple".upper()

def encrypt(msg,shift_no):
    msg_list=list(msg)
    msg_encrypt=[]
    for s in msg_list:
        if s==" ":
            msg_encrypt.append("-")
        else:
            cc=((ord(s)-65)+shift_no)%26
            cch=chr(cc+65)
            msg_encrypt.append(cch)
    return "".join(msg_encrypt)



def decrypt(msg,shift_no):
    msg_list=list(msg)
    msg_encrypt=[]
    for s in msg_list:
        if s=="-":
            msg_encrypt.append(" ")
        else:
            cc=((ord(s)-65)-shift_no+26)%26
            cch=chr(cc+65)
            msg_encrypt.append(cch)
    return "".join(msg_encrypt)
    
dd=encrypt(msg,3)
print("ENCRYPT: ",dd)
ee=decrypt(dd,3)
print("DECRYPT: ",ee)

##############################
#Using random shift
shift_no=random.randint(0,26)
print("Genrated SHift is : ",shift_no)
msg="THOR IS STRONGEST AVENGER"
dd=encrypt(msg,shift_no)
print("Encrypted Text: ",dd)
ee=decrypt(dd,shift_no)
print("Decrypted Text: ",ee)