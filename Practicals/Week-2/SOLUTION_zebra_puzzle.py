
import itertools
import time
'''

Solution to the zebra puzzle exercises

'''


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle_gen():
    houses = [first,_,middle,_,_] = [1,2,3,4,5]
    # return a generator expression
    return ((WATER,ZEBRA)
        for(red, green, ivory, yellow, blue) in itertools.permutations(houses)
        if imright(green, ivory)        #6
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in itertools.permutations(houses)
        if Englishman == red           #2
        if Norwegian == first           #10
        if nextto(Norwegian, blue)      #15
        for (cofee, tea, milk, oj, WATER) in itertools.permutations(houses)
        if cofee == green               #4
        if Ukranian == tea              #5
        if milk == middle               #9
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in itertools.permutations(houses)
        if Kools == yellow              #8
        if LuckyStrike == oj            #13
        if Japanese == Parliaments      #14
        for (dog, snails, fox, horse, ZEBRA) in itertools.permutations(houses)
        if Spaniard == dog              #3
        if OldGold == snails            #7
        if nextto(Chesterfields, fox)
        if nextto(Kools, horse)
       )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def zebra_puzzle_fast():
    '''
    Solve the zebra puzzle.  All the constraint tests are done as early as
    possible. This way, the search tree is pruned dramatically.
    
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    Return (None, None) if no solution was found.
    '''

    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    
    # Note that instead of looping  on the 'orderings' list 
    # as in the file 'zebra_puzzle.py', we loop on the iterator. 
    # In case of a very large list, time and space would be saved.
    for red, green, ivory, yellow, blue in itertools.permutations(houses):
        if not imright(green, ivory): # constraint 6
            continue
        for Englishman, Spaniard, Ukranian, Japanese, Norwegian in itertools.permutations(houses):
            if  not Englishman == red: # constraint 2
                continue
            if not Norwegian == first: # constraint 10
                continue
            if not nextto(Norwegian, blue): # constraint 15
                continue
            for coffee, tea, milk, oj, WATER in itertools.permutations(houses):
                 if not coffee == green: # constraint 4
                     continue
                 if not Ukranian == tea: # constraint 5
                     continue
                 if not milk == middle: # constraint 9
                     continue
                 for OldGold, Kools, Chesterfields, LuckyStrike, Parliaments in itertools.permutations(houses):
                     if not Kools == yellow: # constraint 8
                         continue
                     if not LuckyStrike == oj: # constraint 13
                         continue
                     if not Japanese == Parliaments: # constraint 14
                         continue
                     for dog, snails, fox, horse, ZEBRA in itertools.permutations(houses):
                            if (
                                 Spaniard == dog # constraint 3
                                 and OldGold == snails # constraint 7                                 
                                 and nextto(Chesterfields, fox) # constraint 11
                                 and nextto(Kools, horse) # constraint 12
                                 ):
                                return WATER, ZEBRA

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


if __name__ == "__main__":
    

    # g is a generator
    
    t0 = time.time()
    w,z = zebra_puzzle_fast()
    t1 = time.time()
    
    print ('zebra_puzzle_fast:  w, z = {0},{1}'.format(w,z))
    print ('zebra_puzzle_fast search took {0} seconds'.format(t1-t0))
    
    
    # g is a generator
    g = zebra_puzzle_gen()
    
    t0 = time.time()
    w,z = next(g)
    t1 = time.time()
    
    print ('zebra_puzzle_gen: w, z = {0},{1}'.format(w,z))
    print ('zebra_puzzle_gen search took {0} seconds'.format(t1-t0))


