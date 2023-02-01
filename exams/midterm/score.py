def f(x,y):
        return x+y

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """

    wordHL = 0
    wordSHL = 0
    
    for i, v in enumerate(word):

        if v.isupper():
            if i*(ord(v)-64) >= wordHL:
                wordSHL = wordHL
                wordHL = i*(ord(v)-64)
            elif i*(ord(v)-64) >= wordSHL:
                wordSHL = i*(ord(v)-64)

        if v.islower():
            if i*(ord(v)-96) >= wordHL:
                wordSHL = wordHL
                wordHL = i*(ord(v)-96)
            elif i*(ord(v)-96) >= wordSHL:
                wordSHL = i*(ord(v)-96)

    return f(wordHL, wordSHL)

print(score('adD', f))