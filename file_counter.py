def mostFrequentXter(textFile):
    fhandle = open(textFile)
    xterCount = {}
    mostFrequentXter = []

    for line in fhandle:
        line = line.rstrip()
        line = line.replace(' ', '')
        for xter in line:
            xterCount[xter] = xterCount.get(xter, 0) + 1

    for item in xterCount:
        if len(mostFrequentXter) == 0:
            mostFrequentXter.append((item, xterCount[item]))
        if xterCount[item] > mostFrequentXter[0][1]:
            mostFrequentXter.clear()
            mostFrequentXter.append((item, xterCount[item]))

        mostFrequentLetter = {mostFrequentXter[0][0]: mostFrequentXter[0][1]}

    return mostFrequentLetter


result = mostFrequentXter('myInfo.txt')
print('mostFrequentLetter: ', result)
# /////////////////////////////////////


def mostFrequentWord(textFile):
    fhandle = open(textFile)
    wordCount = {}
    mostFrequetWord = []

    for line in fhandle:
        line = line.rstrip()
        line = line.split()
        for word in line:
            wordCount[word] = wordCount.get(word, 0) + 1

    for item in wordCount:
        if len(mostFrequetWord) == 0:
            mostFrequetWord.append((item, wordCount[item]))
        if wordCount[item] > mostFrequetWord[0][1]:
            mostFrequetWord.clear()
            mostFrequetWord.append((item, wordCount[item]))

    mostFrequentWord = {mostFrequetWord[0][0]: mostFrequetWord[0][1]}

    return mostFrequentWord


result = mostFrequentWord('myInfo.txt')
print('mostFrequentWord: ', result)
# /////////////////////////////////////


def countLines(textFile):
    fhandle = open(textFile)
    lineCount = 0

    for line in fhandle:
        line = line.rstrip()
        lineCount = lineCount + 1

    return lineCount


result = countLines('myInfo.txt')
print('Lines: ', result)
# /////////////////////////////////


def countWords(textFile):
    fhandle = open(textFile)
    wordCount = 0

    for line in fhandle:
        line = line.rstrip()
        line = line.split()
        wordCount = wordCount + len(line)

    return wordCount


result = countWords('myInfo.txt')
print('words: ', result)
# /////////////////////////////////


def countXters(textFile):
    fhandle = open(textFile)
    xterCount = 0

    for line in fhandle:
        line = line.rstrip()
        line = line.replace(' ', '')
        for xter in line:
            xterCount = xterCount + 1

    return xterCount


result = countXters('myInfo.txt')
print('xters: ', result)
