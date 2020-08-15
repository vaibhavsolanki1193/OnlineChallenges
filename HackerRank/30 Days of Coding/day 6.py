def EvenOddIndex(instream):

    evenList = list()
    oddList = list()
    index = 0

    for letters in instream:
        if index % 2 != 0:
            oddList.append(letters)
        else:
            evenList.append(letters)
        index += 1

    print(''.join(evenList) + " " + ''.join(oddList))


n = int(input())
stream = []
for i in range (n):
    elem = input()
    stream.append(elem)

length = len(stream)
for i in range (length):
    word = stream[i]
    EvenOddIndex(word)
