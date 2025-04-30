wordstring=''' 
            it was the best of times it was the worst of times. 
            it was the age of wisdom it was the age of foolishness. 
            it was the epoch of belief it was the epoch of incredulity. 
'''
wordstring=wordstring.replace('.','') # remove the period at the end of each sentence
print(wordstring)
wordlist=wordstring.split() # split the sentence into a list of words
print(wordlist)

wordfreq=[] # create an empty list to store the word frequency
wordfreq.append(wordlist.count('times'))
print(wordfreq)