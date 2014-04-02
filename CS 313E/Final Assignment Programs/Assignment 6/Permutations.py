######################################################################
#                                                                    #
#                           Permutations                             #
#                                                                    #
######################################################################

"""This module contains functions to generate all unique permutations
   of a string."""

import math

def countOccurrences( word ):
    # create a list of 26 0s to count occurrences of each
    # letter.
    word = word.lower()
    occurs = [0]*26
    for ch in word:
        i = ord(ch) - ord('a')
        occurs[i] += 1
    return occurs

def howManyPerms( word ):
    """Return the number of permutations and unique
       permutations of a string."""
    word = word.lower()
    n = len( word )
    # count the occurrences of each letter in word.
    occurs = countOccurrences( word )
    # For any letter that recurs, the number of unique
    # permutations is the totalPerms divided by the 
    # factorial of that count. 
    dividend = 1
    for i in range(26):
        if occurs[i] > 1:
            dividend *= math.factorial( occurs[i] )
    totalPerms = math.factorial( n )
    uniquePerms = totalPerms / dividend
    return ( totalPerms, uniquePerms )

# Fixed this so that it doesn't return duplicates. 

def allPermsAux( word, permsSeen ):
    """This function generates all permutations of the 
    input string."""
    if len( word ) <=1:
        yield word
    else:
        for perm in allPermsAux( word[1:], permsSeen ):
            for i in range( len( perm )+1 ):
                newperm = perm[:i] + word[0] + perm[i:]
                if not newperm in permsSeen:
                    permsSeen.append( newperm )
                    yield newperm


def allPerms( word ):
    return allPermsAux( word, [] )
