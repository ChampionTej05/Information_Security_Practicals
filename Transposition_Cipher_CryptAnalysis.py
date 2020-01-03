

def pre_process(msg,round_key):
    data=dict()
    a=list(round_key)
    a.sort()
    # print(a)
    round_num={}
    cc=0
    for ele in enumerate(a):
        t=ele[1]
        try:
            if t in round_num.keys():
                raise TypeError()
            round_num[t]=ele[0]+1
        except :
            raise TypeError("Duplicate Character Key is not Allowed")
            
    # print(round_num)
    for s in round_key:
        data[s]=round_num[s]
#     print(data)  

    import math
    row=math.ceil(len(msg)/len(round_key))

    row=row+1
    column=len(round_key)
#     print("Rowsize : ",row)



    #populate matrix of size row*column
    table=[["$"]*column for i in range(row)]
    idx=0
    val=list(data.values())
    # print(val)
    while idx<len(val):
        table[0][idx]=val[idx]
        idx=idx+1

#     print("Initial Table")
#     printTable(table)
    return table,data

def printTable(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j],end=' ')
        print(" ")

def encrypt(msg,round_key):
    msg=msg.upper().replace(" ","")
    idx=0
    table,data=pre_process(msg,round_key)
    row=len(table)
    column=len(table[0])
#     print("MSG LEN: ",len(msg))
    #Arrange the msg row-wise
    for i in range(1,row):
        flag=False
        for j in range(column):
    #         print(i,j,idx)
            table[i][j]=msg[idx]
            idx=idx+1
            if idx==len(msg):
                flag=True
                break           
        if flag:
            break

#     printTable(table)
    #creating the cipher by reading column-wise
    cipher_text=""
    for ele in range(len(round_key)):
        ele=ele+1
        idx=0
        for i in range(column):
            if table[0][i]==ele:
                idx=i
                break
    #     print(idx)
    #     print(row)
        for j in range(1,row):
    #         print(j)
            tt=table[j][idx]
            cipher_text=cipher_text+tt
#     print("Cipher Text: ",cipher_text)
    return cipher_text

def decrypt(msg,round_key):
    table,data=pre_process(msg,round_key)
    row=len(table)
    column=len(table[0])
#     print("Encrypted MSG LEN: ",len(msg))
    idx_c=0
    #Insert Column wise
    for ele in range(len(round_key)):
        ele=ele+1
        idx=0
        for i in range(column):
            if table[0][i]==ele:
                idx=i
                break
        
        for j in range(1,row):
            table[j][idx]=msg[idx_c]
            idx_c+=1
#         print("Partial: ",ele)
#         printTable(table)
#     printTable(table)
    
    decipher_text=""
    #Read Row wise
    for i in range(1,row):
        for j in range(column):
            decipher_text+=table[i][j]
#     print("Decipher Text: ",decipher_text)
    return decipher_text
        


from itertools import permutations 
def findPermutation(str):
    alist=list(permutations(str))
    permutationList=list()
#     print(permutationList)
    for p in alist:
        permutationList.append("".join(p))
#     print(permutationList)
    return permutationList
	
cipher="anXdcd8o0s1Xo0i0ewXaXrepdrornhe1tnX".upper()
print(len(cipher))

aa=findPermutation("ABCDEFG")
print(len(aa))


for perm in findPermutation("ABCDEFG"):
    dec1=decrypt(cipher,perm)
    dec2=decrypt(dec1,perm)
#     print("{} => {}".format(dec2,perm))
	#Check for each individual DEC2, whether it is meanigful or not by uncommenting above statement
	