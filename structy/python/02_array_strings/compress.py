"""
Write a function, compress, that takes in a string as an argument. The
function should return a compressed version of the string where consecutive
occurrences of the same characters are compressed into the number of
occurrences followed by the character. Single character occurrences should not
be changed.

'aaa' compresses to '3a' 'cc' compresses to '2c' 't' should remain as 't'

You can assume that the input only contains alphabetic characters.

Notes:
    * n: len(s)
    * Time: O(n)
    * Space: O(n)
"""


def compress(s: str) -> str:
    s += "!"
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num) + s[i])
            i = j
    return "".join(result)
