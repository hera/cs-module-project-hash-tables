def caesar(input_file):
    def sel_sort(arr):
        # loop through n-1 elements
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            
            for j in range(cur_index + 1, len(arr)):
                if arr[j][1] < arr[smallest_index][1]:
                    smallest_index = j

            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        return arr

    with open(input_file) as f:
        encoded_text = f.read()

    encode_table = {
        "E": 11.53,
        "T": 9.75,
        "A": 8.46,
        "O": 8.08,
        "H": 7.71,
        "N": 6.73,
        "R": 6.29,
        "I": 5.84,
        "S": 5.56,
        "D": 4.74,
        "L": 3.92,
        "W": 3.08,
        "U": 2.59,
        "G": 2.48,
        "F": 2.42,
        "B": 2.19,
        "M": 2.18,
        "Y": 2.02,
        "C": 1.58,
        "P": 1.08,
        "K": 0.84,
        "V": 0.59,
        "Q": 0.17,
        "J": 0.07,
        "X": 0.07,
        "Z": 0.03
    }

    decode_table = {}

    occurencies = {}

    # count letter occurencies
    for char in encoded_text:
        if char in encode_table:
            if char in occurencies:
                occurencies[char] += 1
            else:
                occurencies[char] = 1

    # count occurence ratio for each letter
    for char in occurencies:
        decode_table[char] = occurencies[char] / len(encoded_text)


    # convert all items to format [("A", 0.5), ...] and sort

    encode_table_sorted = list(encode_table.items())
    sel_sort(encode_table_sorted)

    decode_table_sorted = list(decode_table.items())
    sel_sort(decode_table_sorted)

    # match letters in encode table with letters in decode table
    match_table = {}

    for i in range(len(decode_table_sorted)):
        match_table[decode_table_sorted[i][0]] = encode_table_sorted[i][0]

    
    # decipher text
    result = []
    for char in encoded_text:
        if char in match_table:
            # letters
            result.append(match_table[char])
        else:
            # dots, commas, etc
            result.append(char)
    
    return "".join(result)




if __name__ == "__main__":
    print(caesar("ciphertext.txt"))