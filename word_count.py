def words(string):
    wordstr = string.split()
    # a list of words is returned then convert it to set to hold only unique items
    unique_words = set(wordstr)
    
    wordict = {} # dictionary to holds the word against count
    for word in unique_words: 
        count = 0
        # Take a unique word and test how many times it occurs in the
        # original list
        for duplicate in wordstr:
            if duplicate == word:
                count +=1 
        if word.isdigit():
            word = int(word)
        wordict[word] = count
    return wordict