'''Fibbonacci'''


def fibbonacci(numOfTerms, retVal = "sequence"):
    '''Fibbonacci function
    Params:
        numOfTerms => Number term to be calculated
        retVal => The desired return value of a function
                  'sequence' -> Prints the sequence
                  'number' -> The last value of calculated term'''
    
    fibboNum = 0
    nextTerm = 1
    nthTerm = 0
    
    if numOfTerms <= 0: print ("Please enter a positive integer")

    elif numOfTerms == 1: print (0)

    else:
        for iterationCount in range(numOfTerms):
            
            nthTerm = fibboNum + nextTerm
            fibboNum = nextTerm
            nextTerm = nthTerm
