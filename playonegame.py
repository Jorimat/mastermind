import numpy as np
import functions as func
from collections import Counter



#Input

codelength = 4
nchars = 6
cheat = True

chars = [str(i) for i in list(range(nchars))]

target = ''.join(np.random.choice(chars, codelength))
print('Target:', target)




def all_codes(chars, codelength):
    '''
    Generate all possible codes
    
    '''
    nchars_ = len(chars)
    ncodes = nchars_**codelength
    codes = []
    mat = []

    for i in range (codelength):
        step =  (nchars_**i)
        short  = sum([[char]*step for char in chars],[])
        nrep = ncodes//len(short)
        long = sum([short for i in range(nrep)], [])
        mat.append(long)

    for i in range(ncodes):
        codes.append(''.join([m[i] for m in mat]))
        
    return sorted(codes)








#Score table
        
class score_table:

    def __init__(self, codes):
        self.codes = np.array(codes)
        self.ncodes = len(codes)
        self.black = np.nan
        self.white = np.nan
        self.enthropy = np.nan

        
    def calc_scores(self):
        ncodes = len(self.codes)

        black = np.zeros((ncodes, ncodes))
        white = np.zeros((ncodes, ncodes))

        for i in range(ncodes):
            for j in range(ncodes):
#                score_ = func.evaluate(guess[i], target[j])
                score_ = func.evaluate(self.codes[i], self.codes[j])
                black[i,j] = score_[0]
                white[i,j] = score_[1]  
                
        self.black = black
        self.white = white
        
        
        
    def calc_enthropy(self):
        '''
        Calculate the score enthropy for each row
        
        '''
#        ncodes = len(self.codes
        if self.ncodes > 1:
            enthropy = []
            for r in range(self.ncodes):
                rowscore = list(zip([b for b in self.black[r]], [w for w in self.white[r]]))
                rowcounts = list(Counter(rowscore).values())
                enthropy.append(sum([c*(self.ncodes-c)/self.ncodes**2 for c in rowcounts]))

            self.enthropy = enthropy
        
        elif self.ncodes == 1:
            self.enthropy = [0]
        
        
    def keep_rows_cols(self, indices):
        '''
        Input: list of indices to keep
        Remove 
        - rows and colums of black and white
        - elements of codes
        Recalculate
        - ncodes
        - enthropy
        '''
        self.black = self.black[keep, :][ :, keep]
        self.white = self.white[keep, :][ :, keep]
        self.codes = self.codes[keep]
        self.ncodes = len(self.codes)
        self.calc_enthropy()       
        
        
        
    def print_table(self):
        '''
        Display score matrix with codes and enthropies
        '''
        print('\n\t' + '\t'.join(self.codes))
        for i in range(self.ncodes):
#            print (self.codes[i], '\t'.join(self.black[i]))
            line = self.codes[i] + '\t' 
            line += ('\t'.join([str((int(self.black[i,j]), int(self.white[i,j]))) for j in range(self.ncodes)]))
            line += '\t' + str(self.enthropy[i])
            print(line)
        
        
        
#Create score table        
scores = score_table(all_codes(chars, codelength))
scores.calc_scores()   
scores.calc_enthropy()




#Display score matrix with codes and enthropies
#scores.print_table()
guesscount = 0

#WHILE LOOP SHALL START HERE
while scores.ncodes > 1:
    guesscount += 1
    print('\n\nGuesses:', guesscount)


    #Pick one the rows with the highest enthropy
    ent = scores.enthropy
    maxent = max(ent)
    candidates = [e for e in range(len(ent)) if ent[e]==maxent]
    iguess = np.random.choice(candidates)
    print('Guess:', scores.codes[iguess])


    #Ask score for the corresponding guess (black, white)
    score = func.evaluate(scores.codes[iguess], target)
    print('Score:', score)


    #Remove appropriate rows and cols
    if score != (codelength, 0):
        keep = [j for j in range(scores.ncodes) if scores.black[iguess][j] == score[0] and scores.white[iguess][j]==score[1]]
    else:
        keep = [iguess]

    print('Keep:', keep)    
    scores.keep_rows_cols(keep)


    #Display score matrix with codes and enthropies
#    scores.print_table()


print('\nCHECK:', target, scores.codes)
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
#Maak gebruik van symmetrie van black en white om ze sneller te berekenen
#Beter verpakken
#Eerste berekening van black en white kost meeste, maar is altijd hetzelfde als de codes niet veranderen.  Dus misschien in file opslaan.