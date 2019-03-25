import numpy as np
import functions as func



#Input

maxtries = 3
codelength = 4
nchars = 2
cheat = True

chars = [str(i) for i in list(range(nchars))]




#Start game
target = ''.join(np.random.choice(chars, codelength))
win = False



#Read in strings from command line, store in list, display all
tries = []
scores = [] 


while len(tries) < maxtries and not win: 

    prompt = func.makePrompt(codelength, target, tries, scores, cheat)
        
    text = input(prompt)
    if text == target:
        win = True
    
    if func.checkguess(text, codelength, chars):
        tries.append(text)
        scores.append(func.evaluate(target, text))
        
    else:
        print('Wrong input format')

    
    
print('\nResult:')
print(func.makePrompt(codelength, target, tries, scores, cheat))
if win:
    print('YOU WIN')
    
else:
    print('COMPUTER WINS')

