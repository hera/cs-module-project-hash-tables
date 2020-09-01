def no_dups(s):
    word_list = s.split(" ")

    # if there's only one word, return it
    if len(word_list) == 1:
        return s

    uniques = {}

    # False means a word hasn't been used yet
    for word in word_list:
        uniques[word] = False
    
    result_list = []

    for word in word_list:
        if word in uniques and uniques[word] == False:
            result_list.append(word)
            # mark this word as used. next time we'll skip it
            uniques[word] = True

    return " ".join(result_list)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))