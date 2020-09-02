import random

def markov(input_file, sentences_max = 5):
    """
        Generate gobbledegook sentences that look real while making absolutely no sense
    """

    # Read in all the words in one go
    with open(input_file) as f:
        text = f.read()


    raw_words = text.split(" ")

    table = {}
    
    for i in range(len(raw_words)):
        word = raw_words[i]
        # save a word if found first time
        if word not in table:
            table[word] = []
        
        # if that word is not the last
        if i < len(raw_words) - 1:
            # if current word has never been followed by the next word, save it in the list
            if raw_words[i + 1] not in table[word]:
                table[word].append(raw_words[i + 1])
    
    unique_words = list(table.keys())

    sentences_done = 0

    while sentences_done != sentences_max:
        result = []

        # find a start word
        for i in range(len(unique_words)):

            word = random.choice(unique_words)

            # if a word starts with a capital letter
            # or it starts with a quote character and a capital letter,
            # it's a start word
            if word[0].isupper() or (len(word) >= 2 and word[0] == "\"" and word[1].isupper()):
                result.append(word)
                break
        
        # keep appending words, until reach a stop word

        for i in range(len(unique_words)):
            # look up in table and pick a random word that can go next
            following_word = random.choice(table[result[-1]])

            # skip start words
            if following_word[0].isupper() or (len(word) >= 2 and following_word[0] == "\"" and following_word[1].isupper()):
                continue

            result.append(following_word)

            # check if that's a stop word
            # stop words are words that end in any of the punctuation .?!,
            # or that punctuation followed by a "
            stop_chars = ["?", "!", "."]

            # if that's a stop word, finish sentence
            if following_word[-1] in stop_chars or len(following_word) >= 2 and following_word[-1] == "\"" and following_word[-2] in stop_chars:
                break
        
        sentence = (" ".join(result)).replace("\n\n", "")
        sentence = (" ".join(result)).replace("\n", " ")
        
        print(sentence + "\n\n", end="")

        # update counter
        sentences_done += 1


if __name__ == "__main__":
    markov("input.txt")