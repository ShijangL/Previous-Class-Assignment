from os import system
system('cls')

def string_count(sentence):
    strlist = []
    evenlist = []
    oddlist = []
    for letters in sentence:
        strlist.append(letters)
    #Separate the senetence into a list of character
    if len(strlist)%2:
        strlist.append(0)
    #Determine if the senetence length is even or odd and make it even
    for i in range(len(strlist)):
        if strlist[i] == ' ':
            strlist[i] = '*'
        if i%2:
            oddlist.append(strlist[i])
        else:
            evenlist.append(strlist[i])
    #Separate the list of characters into odd or even
    return oddlist,evenlist
def construct(odd,even):
    newlist = []
    k = 0
    l = 0
    oddlist = []
    evenlist = []
    for letters in odd:
        oddlist.append(letters)
    for characters in even:
        evenlist.append(characters)
    for i in range(len(oddlist)+len(evenlist)):
        if i%2:
            newlist.append(oddlist[l])
            l += 1
        else:
            newlist.append(evenlist[k])
            k += 1
    for k in range(len(newlist)):
        if newlist[k] == '*':
            newlist[k] = ' '
        if newlist[k] == 0 or newlist[k] == '0':
            del newlist[k]
    original = ''.join(newlist)
    return original
def main():
    """text = input('Please Enter the Sentence to be Encrypted ')
    print(string_count(text)[0])
    print()
    print(string_count(text)[1])"""
    evens = 'Ia**ohmr'
    odds = '*maspooe'
    print(construct(odds,evens))

if __name__ == '__main__':
    main()

    