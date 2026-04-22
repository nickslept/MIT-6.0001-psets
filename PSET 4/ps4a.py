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
    # if length of SEQ == 1 #base case
        # return [sequence]
    # if the length of SEQ > 1: (e.g. meats) 
        #current_permutations = get_permutations(sequence[1:]) #meats --> eats, ats, ts, s; catches the previous permutations
        #new_permutations = [] #different in each scope
    # for loop over each word in current permutations (5, 4, 3, 2, 1)
        # new_permutations.add(current_first_char + word[0:])
        # for loop from 1 to length of word #might need to be len -1
            # new_permutations.add(word[0:i] + current_first_char + [i:])
        # new_permutations.add(word[0:len(word) + current_first_char])
    # return new_permutations

    
    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

