def checkPrimitiveRoot(N,R):
    alist=dict.fromkeys(range(N), False)
    #loop through values from 0 to N-2 
    for i in range(N-1):
        temp=pow(R,i,N)
        if alist[temp]==False:
            alist[temp]=not alist[temp]
        else:
#             print("NOT ROOT at ",i)
            return False
    return True 
	
checkPrimitiveRoot(11,3)



#finds all possible Primitive roots

def findRoot(N):
    collectRoots=[]
    #Try out all possible values between 1 to N-1
    for i in range(1,N,1):
        if checkPrimitiveRoot(N,i):
            print("{} is the Primitive Root module  {}".format(i,N))
            collectRoots.append(i)
            
#     print("NO ROOT Exists ")
    return collectRoots
	
	
findRoot(11)



#Generate discrete log table 


#works only when g is Primitive ROOT OF G
def generateDiscreteLogTable(N,g):
    collectRoots=findRoot(N)
    if g not in collectRoots:
        print(" {} not Root of {}".format(g,N))
        return 
    table=dict.fromkeys(range(1,N),0)
    for i in range(N-1):
        temp=pow(g,i,N)
        table[temp]=i
       
    print("TABLE FOR DISCRETE LOGARITHM OF {} under module {}".format(g,N))
    print("N\tLog(g)[N]")
    for k,v in table.items():
        print("{}\t{}".format(k,v))
        
		
generateDiscreteLogTable(11,2)