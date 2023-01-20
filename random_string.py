'''Creates a pseudo random string generator'''

import random

def create_random_str(phrase_seed, salt = '', str_length = 15):
    
    seed = create_seed(phrase_seed, salt)
    random.seed(seed)
    ucode = [33, 126]
    random_string = ''

    for i in range(str_length):
        random_string += chr(random.randint(ucode[0], ucode[1]))

    return random_string

def create_seed(phrase, salt = ''):
    '''Create random seeds that will later be combined
    for the randomization'''
    
    rand_upper_bound = 999
    subseed_collection = []
    final_seed = 0
    volatile_seed = 0
    
    for char in str(salt)+phrase:
        random.seed(ord(char) + volatile_seed)
        volatile_seed = random.randint(0, rand_upper_bound)
        subseed_collection.append(volatile_seed)

    print(f'Sub seed collection {subseed_collection}')

    for i in subseed_collection:
        final_seed += i
        
    return final_seed


def TEST_verify_seeds(trials):
    '''Test function for checking if
    the seeds generated are consistent'''
    
    phrase = "demeligato"
    isConsistent = True
    trial_index = 0
    TEST_seed_consistency = []
    for i in range(trials):

        TEST_seed_consistency.append( create_seed(phrase) )

    initial_sample = TEST_seed_consistency[0]

    for i, seed in enumerate(TEST_seed_consistency):
        
        if seed != initial_sample:
            trial_index = i
            isConsistent = False
            break
        
        print(f'Testing seed {seed}')
        print(f'Trial no. {i}, consistency result {isConsistent}')

    print(f'Tested {trials} times', end=' ')
    if isConsistent:
        print('No inconsistency found', end='\n')
    else:
        print(f'Found inconsistency in trial index {trial_index}', end='\n')
        

def TEST_verify_random_str(trials):
    '''Test function for checking if the
    pseudo-randomly generated string are consistent'''
    
    phrase = "demeligato"
    isConsistent = True
    trial_index = 0
    TEST_pseudo_random_consistency = []
    for i in range(trials):
        TEST_pseudo_random_consistency.append(
            create_random_str(phrase, i)
        )
        
    initial_sample = TEST_pseudo_random_consistency[0]
    print(f'Initial sample: {initial_sample}')
    for i, randstr in enumerate(TEST_pseudo_random_consistency):

        if randstr != initial_sample:
            trial_index = i
            isConsitent = False
##            break

        print(f'Random str output {randstr}')
        print(f'Trial no. {i}, consistency result {isConsistent}')

    print(f'Tested {trials} times', end=' ')
    if isConsistent:
        print('No inconsistency found', end='\n')
    else:
        print(f'Found inconsistency in trial index {trial_index}', end='\n')
        
        
##TEST_verify_seeds(100)
TEST_verify_random_str(100)
##x = create_seed("demeligato")
##c = create_random_str('demeligato','',20)
##print(x)
##print(c)

##for i in range (32, 126+1):
##    print(chr(i))

##for i in range(1000):
##    print(random.randint(0,3))
##    random.seed(601)
##    print(random.randint(32,126))
