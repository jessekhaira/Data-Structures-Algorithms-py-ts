def knuthMorrisPratt(bigstr, substr):
    """
    This algorithm represents the Knuth-Morris-Pratt(KMP) string-searching algorithm. This algorithm is used to search
    for occurrences of a word X within another word Y.

    Best/avg/worst:
        Time: O(n+m) 
        Space: (m) 

    Where n is the length of string1, m is the length of the string your looking
    for in string1. 
    
    Inputs:
        - bigstr (String):
        - substr (String):

    Returns:
        - Integer indicating where the substr starts within the bigstr. If not found, function will return -1. 
    """
    prefixSuffixTable = makePrefixSuffixTable(substr)
    return match(bigstr, substr, prefixSuffixTable)

def makePrefixSuffixTable(substr):
    table = [-1] * len(substr)
    i = 0
    j = 1
    while j < len(substr):
        if substr[j] == substr[i]:
            table[j] = i 
            j += 1
            i += 1
        elif i != 0:
            i = table[i-1] + 1
        else:
            j += 1
    return table

def match(bigstr, substr, prefixSuffixTable):
    i = 0
    j = 0
    while i < len(bigstr) and j < len(substr):
        if bigstr[i] == substr[j]:
            i += 1
            j += 1
        elif j != 0:
            j = prefixSuffixTable[j-1] + 1
        else:
            i += 1
    return i-j if j == len(substr) else -1 

