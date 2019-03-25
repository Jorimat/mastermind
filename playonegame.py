import numpy as np
from collections import Counter

import functions as func
from classes import *


#Input

codelength = 4
nchars = 4
cheat = True

chars = [str(i) for i in list(range(nchars))]

target = ''.join(np.random.choice(chars, codelength))
print('Target:', target)






        
#Create score table        
#scores = score_table(func.all_codes(chars, codelength))
scores = score_table(chars, codelength)
scores.calc_scores()   
scores.calc_enthropy()




#Display score matrix with codes and enthropies
#scores.print_table()
guesscount = 0

#WHILE LOOP SHALL START HERE
while scores.ncodes > 1:
    guesscount += 1
#    print('\n\nGuesses:', guesscount)


    #Pick one the rows with the highest enthropy
    ent = scores.enthropy
    maxent = max(ent)
    candidates = [e for e in range(len(ent)) if ent[e]==maxent]
    iguess = np.random.choice(candidates)
#    print('Guess:', scores.codes[iguess])


    #Ask score for the corresponding guess (black, white)
    score = func.evaluate(scores.codes[iguess], target)
#    print('Score:', score)
    print(scores.codes[iguess], score)


    #Remove appropriate rows and cols
    if score != (codelength, 0):
        keep = [j for j in range(scores.ncodes) if scores.black[iguess][j] == score[0] and scores.white[iguess][j]==score[1]]
    else:
        keep = [iguess]

#    print('Keep:', keep)    
    scores.keep_rows_cols(keep)


    #Display score matrix with codes and enthropies
#    scores.print_table()


print('CHECK:', target, scores.codes)
print('Guesses:', guesscount)

        
        

##Print sorted enthropy list
#ncodes = len(scores.codes)
#enthropylist = [(scores.codes[c], scores.enthropy[c]) for c in range(ncodes)]  
#enthropylist = sorted(enthropylist, key=lambda x: x[1])    
#for e in enthropylist:
#    print(e[0], round(e[1],5))
#        
#
#        
#        
##Pick some rows and cols to remove
#remove = [1,3]
#scores.remove_rows_cols(indices)
#
#
#
##Print sorted enthropy list
#ncodes = len(scores.codes)
#enthropylist = [(scores.codes[c], scores.enthropy[c]) for c in range(ncodes)]  
#enthropylist = sorted(enthropylist, key=lambda x: x[1])    
#for e in enthropylist:
#    print(e[0], round(e[1],5))  



#TO DO
#Eerste berekening van black en white kost meeste, maar is altijd hetzelfde als de codes niet veranderen.  Dus misschien in file opslaan.