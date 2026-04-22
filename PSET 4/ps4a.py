# Problem Set 4A

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    current_first_char = sequence[0]
    if len(sequence) == 1: #base case (e.g. s in meats)
        return [sequence]
    if len(sequence) > 1: #(e.g. meats) 
        current_permutations = get_permutations(sequence[1:]) #meats --> eats, ats, ts, s; catches the previous permutations
        new_permutations = [] #different in each scope
        for word in current_permutations: # e.g. when current_first_char in meats in a then curr perms = [ts, st]
            new_permutations.append(current_first_char + word) #handles placing current_first_char at the beginning of the word
            for i in range(1, len(word)): #handles placing current_first_char in spots in the middle of the word
                new_permutations.append(word[0:i] + current_first_char + word[i:])
            new_permutations.append(word + current_first_char) #handles placing current_first_char at the end of word
    return new_permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print('Input:', "a")
    print('Expected Output:', ["a"])
    print('Actual Output:', get_permutations("a"))

    print('Input:', "ab")
    print('Expected Output:', ["ab", "ba"])
    print('Actual Output:', get_permutations("ab"))

    print('Input:', "abc")
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations("abc"))


