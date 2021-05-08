""" This module contains code representing the Knuth-Morris-Pratt string
search algorithm """


def knuth_morris_pratt(bigstr: str, substr: str) -> int:
    """ This algorithm represents the Knuth-Morris-Pratt(KMP) string-search
    algorithm. This algorithm is used to search for occurrences of a word X
    within another word Y.

    Time:
        O(N+M) best/avg/worst

    Space:
        O(M) best/avg/worst

    Where N is the length of bigstr, M is the length of substr.

    Args:
        bigstr:
            String representing the string we are looking for the pattern substr
            within

        substr:
            String representing the string we are looking for within the bigstr

    Returns:
        Integer indicating where the substr starts within the bigstr. If not
        found, the function will return -1.

    """
    if not substr:
        return -1
    prefix_suffix_table = make_prefix_suffix_table(substr)
    return match(bigstr, substr, prefix_suffix_table)


def make_prefix_suffix_table(substr):
    table = [-1] * len(substr)
    i = 0
    j = 1
    while j < len(substr):
        if substr[j] == substr[i]:
            table[j] = i
            j += 1
            i += 1
        elif i != 0:
            i = table[i - 1] + 1
        else:
            j += 1
    return table


def match(bigstr, substr, prefix_suffix_table):
    i = 0
    j = 0
    while i < len(bigstr) and j < len(substr):
        if bigstr[i] == substr[j]:
            i += 1
            j += 1
        elif j != 0:
            j = prefix_suffix_table[j - 1] + 1
        else:
            i += 1
    return i - j if j == len(substr) else -1
