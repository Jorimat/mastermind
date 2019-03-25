#X = 123456789
#Y = 362436069
#Z = 521288629
#W = 88675123
#
#def xor_shift():
#    global X, Y, Z, W
#    t = X ^ (X << 11)
#    X = Y
#    Y = Z
#    Z = W
#    W = W ^ (W >> 19) ^ t ^ (t >> 8)
#    return W
#
#
#def randint(imax):
#    W1 = xor_shift()
#    return W1%(imax+1)
#    
#for i in range(10):
#    print(randint(1))
#    
##W2 = xor_shift() # 646616338854
##W3 = xor_shift() # 476657867818
##
##print(W1, W2, W3)

#imax = 10
#
#text = 'default'
#num = 0
#while text == 'default':
##    text = input('Press enter')
#    num +=1
#    num = num%(imax+1)
#    
#    
#print(num)    
    

    
    
    
##Random function
#
#def randomint(imax, bytesfile):
#
#    if imax < 2**8:
#
#        #Read in bytes
#        with open(bytesfile, "rb") as f:
#            randombytes = f.read()
#
#        res = randombytes[0]%(imax+1)
#
#        #push these bits to the end of randombytes
#        randombytes =  randombytes[1:] + bytes([randombytes[0]])
#
#        #write the new randombits to 'random.bin'
#        with open(bytesfile, "wb") as f:
#            f.write(randombytes)    
#
#        return res
#
#    else:
#        print('ERROR')
#    
#
#    
#for i in range(5):
#    print(randomint(imax = 10, bytesfile = "random.bin" ))



#Counter
def counter(x):
    counts = {}
    for i in set(x):
        counts[i] = sum([t==i for t in x])
    return counts



