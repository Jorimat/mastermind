#Same functionality as main.py, but independent from modules


#Input

maxtries = 3
codelength = 4
nchars = 2
cheat = True

chars = [str(i) for i in list(range(nchars))]



def makePrompt(codelength, target, tries, cheat):
    prompt = "\n" + '*'*codelength
    if cheat:
        prompt += '(' + target + ')'
    prompt +=  '\n'   
        
    for t in range(len(tries)):
        prompt += tries[t] + '\t' + 'o'*scores[t][0] + 'i'*scores[t][1] + '\n'
        
    return prompt


def evaluate(target, guess):
    # Count black points
    black = sum([target[i]==guess[i] for i in range(len(target))])
   
    # Count white points 
    tcounts = counter(target)
    gcounts = counter(guess)
    keys = [k for k in tcounts.keys() if k in gcounts.keys()]
    overlap = sum([min(tcounts[k], gcounts[k]) for k in keys])
    white = overlap - black
    
    return ((black, white))



def checkguess(guess, codelength, chars):
    # Check length
    if len(guess) != codelength:
        return False
    
    # Check chars
    elif not all([g in chars for g in set(guess)]):
        return False
    
    else:    
        return True
    

    
#Pseudo-random int generator
def randomint(imax, bytesfile):
    if imax < 2**8:

        #Read in bytes
        with open(bytesfile, "rb") as f:
            randombytes = f.read()

        res = randombytes[0]%(imax+1)

        #push these bits to the end of randombytes
        randombytes =  randombytes[1:] + bytes([randombytes[0]])

        #write the new randombits to 'random.bin'
        with open(bytesfile, "wb") as f:
            f.write(randombytes)    

        return res

    else:
        print('ERROR')    
        
        
        
#Counter
def counter(x):
    counts = {}
    for i in set(x):
        counts[i] = sum([t==i for t in x])
    return counts        
    


#Start game
target = ''
for j in range(codelength):
    target += str(randomint(imax=nchars-1, bytesfile = 'random.bin'))
win = False
tries = []
scores = [] 


#Read in strings from command line, store in list, display all
while len(tries) < maxtries and not win: 

    prompt = makePrompt(codelength, target, tries, cheat)
        
    text = input(prompt)
    if text == target:
        win = True
    
    if checkguess(text, codelength, chars):
        tries.append(text)
        scores.append(evaluate(target, text))
        
    else:
        print('Wrong input format')

    
#End of game    
print(makePrompt(codelength, target, tries, cheat))
if win:
    print('YOU WIN')
    
else:
    print('COMPUTER WINS')

