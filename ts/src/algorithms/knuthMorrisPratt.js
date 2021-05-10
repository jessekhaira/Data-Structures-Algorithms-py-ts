/**
 * This algorithm represents the Knuth-Morris-Pratt(KMP)
 * string-searching algorithm. This algorithm is used to search
 * for occurrences of a word X within another word Y.
 * 
 * Time: O(n+m)
 * Space: (m)
 * 
 * Where n is the length of string1, m is the length of the string your looking
 * for in string 1.
 * 
 * @param {string} bigstr 
 * @param {string} substr 
 * @returns {number} Number indicating where the substr starts within the bigstr
 * . If not found, function will return -1. 
 */
function knuthMorrisPratt(bigstr, substr) {
    const prefixSuffixTable = makePrefixSuffixTable(substr);
    return match(bigstr, substr, prefixSuffixTable);
}

function makePrefixSuffixTable(substr) {
    // pointer i always moves forward
    let i = 1;
    // pointer j moves forward until match is not found
    // and then moves backward intelligently. 
    let j = 0;

    const table = Array(substr.length).fill(-1);
    while (i< substr.length) {
        if (substr[i] === substr[j]) {
            table[i] = j;
            j++;
            i++;
        }
        else if (j !== 0) {
            j = table[j-1]+1;
        }
        else {
            i++;
        }

    }
    return table; 
}

function match(bigstr, substr, prefixSuffixTable) {
    // pointer i used within the bigstr. i always moves forward
    let i = 0;
    // pointer j used within the substr. j moves forward until match is not found
    // and then moves backward intelligently
    let j = 0;

    while (i < bigstr.length && j<substr.length) {
        if (bigstr[i] === substr[j]) {
            i++;
            j++;
        }
        else if (j !== 0) {
            j = prefixSuffixTable[j-1]+1;
        }
        else {
            i++;
        }
    }
    return (j === substr.length ? i-j: -1);
}