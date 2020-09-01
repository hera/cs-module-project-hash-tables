
def word_count(s):
    if len(s) == 0:
        return {}

    # get rid of these characters
    ignored_chars = ["\"", ":", ";", ",", ".", ",", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    for char in ignored_chars:
        s = s.replace(char, "")

    for char in ("\t", "\r", "\n"):
        s = s.replace(char, " ")

    words = s.split(" ")
    result = {}

    for word in words:
        if len(word) == 0:
            continue

        word_lower = word.lower()

        if word_lower in result:
            result[word_lower] += 1
        else:
            result[word_lower] = 1
    
    return result

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))