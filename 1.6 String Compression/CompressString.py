'''
Question 1.6: String Compression - Cracking the Coding Interview, 6th edition
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not
become smaller than the original string, your method should return the original string. You
can assume the string has only uppercase and lowercase letters (a-z).
'''


def CompressString(string: str) -> str:
    compressed = ""
    count = 0
    last = "" if len(string) == 0 else string[0]
    for char in string:
        if char == last:
            count += 1
        else:
            compressed += last + str(count)
            last = char
            count = 1
    compressed += last + str(count)

    if len(string) < len(compressed):
        return string
    else:
        return compressed
