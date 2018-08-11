#find a path within the graph from start node to end node
def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = findPath(graph, node, end, path)
            if newpath: return newpath
    return None

#returns True if a path exists from start node to end node
def pathExists(graph, start, end, path=[]):
    if findPath(graph, start, end) is not None:
        return True
    else: 
        return False

#binary search method to find a word in a list of words 
def findWord(words, word): 
    start = 0
    end = len(words)
    while start < end:
        mid = start + (end - start) // 2
        midpoint = words[mid]
        if word == midpoint:
            return mid
        elif word > midpoint:
            if start == mid: 
                break
            start = mid
        elif word < midpoint:
            end = mid

#returns True if a word exists in the sowpod list. 
def wordExists(wordlist, word): 
    w = word.upper()
    l = sorted(wordlist) #ensures optimized findWord method

    return findWord(l, w) != None

#takes a word and returns an array of words with middle characters removed. If a word has even number of letters, returns an array with length 2             
def removeMiddleCharacter(word):
    arr = []
    l = len(word)
    if l <= 2: 
        pass
    elif l % 2 == 1:
        n = l // 2
        m = l // 2 + 1
        wordminusmiddle = word[:n] + word[m:]
        arr.append(wordminusmiddle)
    else:
        n = l // 2 - 1
        m = l // 2 + 1
        wordminusmiddle1 = word[:n + 1] + word[m:]
        wordminusmiddle2 = word[:n] + word[m-1:]
        arr.append(wordminusmiddle1)
        arr.append(wordminusmiddle2)
    return arr

#returns a graph of all possible subWords. The original word serves as the parent, and the child nodes are the new words.
def graphOfPossibleSubwords(graph, wordlist, word):
    arr = []

    #remove the beginning character in word
    wordMinusBeginningChar = word[1:]

    #remove the last character in word
    wordMinusEndChar = word[:-1]

    #remove the middle character(s) in word
    wordsMinusMiddleChars = removeMiddleCharacter(word)

    #base case: reached empty string
    if len(wordMinusBeginningChar) < 1:
        return arr #returns empty array
    else: 
        #check to see if subword exists in dictionary. If it does, add subword to array and find its subwords
        if wordExists(wordlist, wordMinusBeginningChar):
            arr.append(wordMinusBeginningChar)
            graphOfPossibleSubwords(graph, wordlist, wordMinusBeginningChar)
        if wordExists(wordlist, wordMinusEndChar):
            arr.append(wordMinusEndChar)
            graphOfPossibleSubwords(graph, wordlist, wordMinusEndChar)
        for w in wordsMinusMiddleChars:
            if wordExists(wordlist, w):
                arr.append(w)
                graphOfPossibleSubwords(graph, wordlist, w)
    
    #add possible subwords to graph and return the graph
    graph[word] = arr
    return graph
    
# find length of longest word in a list
def findLongestWordLength(wordlist):
    longestlength = 0
    for w in wordlist: 
        l = len(w)
        if l > longestlength: 
            longestlength = l
    return longestlength

# find valid words in a list of certain length
def findWordsOfLength(wordlist, length): 
    arr = []
    for w in wordlist: 
        if len(w) == length:
            if 'O' in w or 'I' in w or 'A' in w:
                arr.append(w)
    return arr

# find the longest word that matches the criteria of Problem 1. Start with the longest words and go down until you find one and return the word
def findLongestSpecialWord(wordlist):
    wordFound = False
    word = ""
    
    #find the length of longest word in the wordlist
    longestWordInDictLength = findLongestWordLength(wordlist)

    # #create a new dictionary with words of that length.
    # newDict = findWordsOfLength(wordlist, longestWordInDictLength)
    
    #starting from the longest word, iterate thru newDict to find a word that matches the criteria. End the loop if word is found
    for numLetters in range(longestWordInDictLength, 1, -1):
        if wordFound:
            break
        else: 
            print("analyzing words of length " + str(numLetters)) #for viz

            #create a new dictionary with words of that length.
            newDict = findWordsOfLength(wordlist, numLetters)

            for entry in newDict:
                entry = entry.lower()
                possibleSubWords = {}

                #build graph of possible subwords
                graphOfPossibleSubwords(possibleSubWords, wordlist, entry)

                #if path to one of the 1 letter words exists, then this is a special word
                pathToOExists = pathExists(possibleSubWords, entry, "o")
                pathToAExists = pathExists(possibleSubWords, entry, "a")
                pathToIExists = pathExists(possibleSubWords, entry, "i")

                #if path exists, break out of loop
                if pathToOExists or pathToAExists or pathToIExists:
                    word = entry
                    wordFound = True
                    break
                else: 
                    print(entry + " is not valid") #for viz
    return word.upper()

#open the txt file and add words to array
file = open("sowpods.txt", "r")
dictionary = file.read().splitlines()
file.close()

#find the longest word that meets the criteria. Print that word
longestWord = findLongestSpecialWord(dictionary)
print(longestWord + " is the longest special word with a length of " + str(len(longestWord)))

#Check work
####################################
# graph = {}
# entry = "CHOREGUSES"
# graphOfPossibleSubwords(graph, dictionary, entry)
# print(findPath(graph, entry, "A"))
# print(findPath(graph, entry, "I"))
# print(findPath(graph, entry, "O"))

# print(findWord(dictionary, "CHOREUSES"))



#TESTS
####################################
# graph = {'A': ['B', 'C'],
#              'B': ['C', 'D'],
#              'C': ['D'],
#              'D': ['C'],
#              'E': ['F'],
#              'F': ['C']}
# words = ["COINS", "TABLE", "FOR", "FORK", "MAT", "SICKLE"]
# print(findPath(graph, 'A', 'D'))  #['A', 'B', 'C', 'D']
# print(pathExists(graph, 'A', 'D'))  #True
# print(findWord(dictionary, "COINS")) #42738
# print(wordExists(dictionary, "coins")) #True
# print(removeMiddleCharacter("coins")) #['cons']
# print(graphOfPossibleSubwords({}, dictionary, "COINS")) #{'ON': ['O'], 'CON': ['ON'], 'COIN': ['CON'], 'OS': ['O'], 'ONS': ['ON', 'OS'], 'COS': ['OS'], 'CONS': ['ONS', 'CON', 'COS'], 'COINS': ['COIN', 'CONS']}
# print(findLongestWordLength(words)) #15
# print(findWordsOfLength(words, 5)) #['COINS', 'TABLE']
# print(findLongestSpecialWord(dictionary)) #AARTI if length is 5