#Functions
from collections import Counter



def makePrompt(codelength, target, tries, scores, cheat):
    prompt = "\n" + '*'*codelength
    if cheat:
        prompt += '(' + target + ')'
    prompt +=  '\n'   
        
    for t in range(len(tries)):
        prompt += tries[t] + '\t' + 'o'*scores[t][0] + 'i'*scores[t][1] + '\n'
        
    return prompt


def evaluate(target, guess):
    
    chars_ = list(set(target+guess))
    
    # Count black points
    black = sum([target[i]==guess[i] for i in range(len(target))])
   
    # Count white points 
    tcounts = Counter(target)
    gcounts = Counter(guess)
    overlap = sum([min(tcounts[c], gcounts[c]) for c in chars_])
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
