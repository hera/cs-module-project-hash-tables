def histogram(input_file):
    def sel_sort(arr):
        """
            Sort an array in ascending order
        """

        # loop through n-1 elements
        for i in range(0, len(arr) - 1):
            cur_index = i
            largest_index = cur_index
            
            for j in range(cur_index + 1, len(arr)):
                if arr[j][1] > arr[largest_index][1]:
                    largest_index = j

            arr[largest_index], arr[cur_index] = arr[cur_index], arr[largest_index]

        return arr

    with open(input_file) as f:
        text = f.read()

    # get rid of these characters
    ignored_chars = [" ", "\n", "!", "?", "\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]


    # extract only words
    words = []
    current_word = ""
    
    for char in text:
        if char in ignored_chars:
            if len(current_word):
                words.append(current_word)
                current_word = ""
        else:
            current_word += char.lower()


    # count occurencies of each word in the text
    occurencies = {}

    for word in words:
        if word in occurencies:
            occurencies[word] += 1
        else:
            occurencies[word] = 1
    
    """
    convert occurencies to format:
    {
        ("the": 12),
        ("only": 34)
    }
    """
    occurencies_sorted = list(occurencies.items())

    # sort in ascending order
    sel_sort(occurencies_sorted)

    # print out all words line by line
    indent = 20

    for word in occurencies_sorted:
        """
        For example:
        wind               ########
        glade              ####
        """
        print(word[0] + " " * (indent - len(word[0])) + "#" * word[1])


if __name__ == "__main__":
    histogram("robin.txt")