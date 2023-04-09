'''Random nonsense word generator'''
##with problems
from random import randint
from time import sleep
from string import capwords

class Bolognafy:
    '''Class for generating nonsense readable words, can be useful for weird names'''
    
    def __init__(self):
        ##initialized variables to be used
        self.g_minWordLength = 3
        self.g_maxWordLength = 14
        self.g_VOWELS = "aeiou"
        self.g_CONSONANTS = "bcdfghjklmnpqrstvwxyz"
        self.g_VOWELCOMBINATIONS = ["ae","ei","ai","ao","au"
                                   ,"ee","eo","eu","ia","ie"
                                   ,"ii","io","oa","oe","oo"
                                   ,"ou","ua","ue","ui",]
        self.g_CONSONANTCOMBINATIONS = ["cc","dd","ch","cl","ck",
                                        "ct","cs","cy","dd","dy",
                                        "ft","ff","fy","ll","gg",
                                        "mm","nd","ng","nt","ld",
                                        "pr","rp","ts","st","ty"]

    def paWordGen(self):
        m_randSeed = randint(1,99990)   ##for deciding the first character
        m_wordLength = randint(self.g_minWordLength,self.g_maxWordLength)    ##for deciding the word length
        m_randWord =""
        m_isLastCharVowel = False
        m_isVowelCombPlaced = False
        m_isConsonantCombPlaced = False
        m_index = 1
        ##create a random first letter then label switch if it is a vowel or not
        if (m_randSeed % 2) ==1:
            m_randWord = self.g_CONSONANTS[randint(0,len(self.g_CONSONANTS)-1)]
        else:
            m_randWord = self.g_VOWELS[randint(0,len(self.g_VOWELS)-1)]
            m_isLastCharVowel = True

        ##for the rest of the word, randomize the chars
        while(m_index <  m_wordLength):
            m_nextChar = ""
            
            ##0 places normal chars, 1 places bigrams also check if bigrams could still fit in
            if randint(0,1) and (m_index+2) <= m_wordLength:
                if m_isLastCharVowel:
                    if not m_isConsonantCombPlaced:
                        m_randWord += self.g_CONSONANTCOMBINATIONS[randint(0,len(self.g_CONSONANTCOMBINATIONS)-1)]
                        m_isConsonantCombPlaced = True
                        m_index += 2
                    else:
                        ##if the consonant bigrams was placed, use a regular consonant instead
                        m_randWord +=  self.g_CONSONANTS[randint(0,len(self.g_CONSONANTS)-1)]
                        m_index += 1
                    
                else:
                    if not m_isVowelCombPlaced:
                        m_randWord += self.g_VOWELCOMBINATIONS[randint(0,len(self.g_VOWELCOMBINATIONS)-1)]
                        m_isVowelCombPlaced = True
                        m_index += 2
                        ##if the vowel bigrams was placed, use a regular vowel instead
                    else:
                        m_randWord +=  self.g_VOWELS[randint(0,len(self.g_VOWELS)-1)]
                        m_index += 1
                
            else:

                ##regular letter was to be placed
                if m_isLastCharVowel:
                    m_randWord +=  self.g_CONSONANTS[randint(0,len(self.g_CONSONANTS)-1)]
                else:
                    m_randWord +=  self.g_VOWELS[randint(0,len(self.g_VOWELS)-1)]
                m_index += 1
                
            m_isLastCharVowel = not m_isLastCharVowel
            
        return capwords(m_randWord)

