import numpy as np
from collections import Counter



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
    tcounts = Counter(target)
    gcounts = Counter(guess)
    overlap = sum([min(tcounts[c], gcounts[c]) for c in chars])
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




#Start game
target = ''.join(np.random.choice(chars, codelength))
win = False



#Read in strings from command line, store in list, display all
tries = []
scores = [] 


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

    
    
print('\nResult:')
print(makePrompt(codelength, target, tries, cheat))
if win:
    print('YOU WIN')
    
else:
    print('COMPUTER WINS')

