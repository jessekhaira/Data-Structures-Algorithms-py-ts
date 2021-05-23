function makePrefixSuffixTable(substr: string): number[] {
    // pointer i always moves forward
    let i = 1;
    // pointer j moves forward until match is not found
    // and then moves backward intelligently.
    let j = 0;

    const table = Array(substr.length).fill(-1) as number[];
    while (i < substr.length) {
        if (substr[i] === substr[j]) {
            table[i] = j;
            j += 1;
            i += 1;
        } else if (j !== 0) {
            j = table[j - 1] + 1;
        } else {
            i += 1;
        }
    }
    return table;
}

function match(
    bigstr: string,
    substr: string,
    prefixSuffixTable: number[],
): number {
    // pointer i used within the bigstr. i always moves forward
    let i = 0;
    /* pointer j used within the substr. j moves forward until
    match is not found and then moves backward intelligently */
    let j = 0;

    while (i < bigstr.length && j < substr.length) {
        if (bigstr[i] === substr[j]) {
            i += 1;
            j += 1;
        } else if (j !== 0) {
            j = prefixSuffixTable[j - 1] + 1;
        } else {
            i += 1;
        }
    }
    return j === substr.length ? i - j : -1;
}

/**
 * This algorithm represents the Knuth-Morris-Pratt(KMP)
 * string-searching algorithm. This algorithm is used to search
 * for occurrences of a word X within another word Y.
 *
 * Time:
 *     O(n+m) best/avg/worst
 * Space:
 *     O(m) best/avg/worst
 *
 * Where n is the length of string1, m is the length of the string
 * your looking for in string 1.
 *
 * @param {string} bigstr String we are looking for the substr pattern in
 * @param {string} substr Pattern we are looking for in the big string
 * @returns {number} Number indicating where the substr starts within the bigstr
 * . If not found, function will return -1.
 */
function knuthMorrisPratt(bigstr: string, substr: string): number {
    if (substr == null || substr.length === 0) {
        return -1;
    }
    const prefixSuffixTable = makePrefixSuffixTable(substr);
    return match(bigstr, substr, prefixSuffixTable);
}
export default knuthMorrisPratt;
