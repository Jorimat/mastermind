import numpy as np
from collections import Counter

import functions as func



#Score table
        
class score_table:

    def __init__(self, chars, codelength):        
        self.codes = np.array(func.all_codes(chars, codelength))
        self.ncodes = len(self.codes)

        
    def calc_scores(self):
        '''
        Make score matrices for all possible combinations of a target (columns) and a guess (rows)
        '''
                
        black = np.empty((self.ncodes, self.ncodes))
        white = np.empty((self.ncodes, self.ncodes))

        for i in range(self.ncodes):
            for j in range(i+1):
                score_ = func.evaluate(self.codes[i], self.codes[j])
                black[i,j] = score_[0]
                black[j,i] = score_[0]                
                white[i,j] = score_[1]
                white[j,i] = score_[1]  
                
        self.black = black
        self.white = white
        
        
        
    def calc_enthropy(self):
        '''
        Calculate the score enthropy for each row
        '''
        
        if self.ncodes > 1:
            enthropy = []
            for r in range(self.ncodes):
                rowscore = list(zip([b for b in self.black[r]], [w for w in self.white[r]]))
                rowcounts = list(Counter(rowscore).values())
                enthropy.append(sum([c*(self.ncodes-c)/self.ncodes**2 for c in rowcounts]))

            self.enthropy = enthropy
        
        elif self.ncodes == 1:
            self.enthropy = [0]
        
        
    def keep_rows_cols(self, keep):
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
        
        