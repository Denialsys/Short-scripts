'''Fibbonacci'''


def fibbonacci(numOfTerms, retVal = "sequence"):
    '''Calculates the fibonacci sequence

    Params:
        numOfTerms => Number term to be calculated
        retVal => The desired return value of a function
                  'sequence' -> Prints the sequence (default)
                  'number' -> The last value of calculated term'''
    
    fibboNum = 0
    nextTerm = 1
    nthTerm = 0
    
    if numOfTerms <= 0: print ("Please enter a positive integer")

    elif numOfTerms == 1:
        if retVal == "sequence": print (0)
        else: return 0

    else:
        for iterationCount in range(numOfTerms):

            ##Check the parameter retVal
            if retVal == "sequence": print (fibboNum, end = ' ')
            elif (retVal == "number" and iterationCount == numOfTerms -1 ):
                return fibboNum

            ##Adjust values
            nthTerm = fibboNum + nextTerm
            fibboNum = nextTerm
            nextTerm = nthTerm
