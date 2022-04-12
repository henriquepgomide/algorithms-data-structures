"""
uncompress

Write a function, uncompress, that takes in a string as an argument. The input
string will be formatted into multiple groups according to the following
pattern:

<number><char>

for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each
'char' of a group is repeated 'number' times consecutively. You may assume
that the input string is well-formed according to the previously mentioned
pattern.


Time Complexity - O(n*m)

Notes:
    * Strings concatenation in python are not linear, as every time you
    add a characters to a string, python will create a copy of that string.
    * The solution is to use a list and the append method, so it add new
    characters in linear time. As the join method is outside the loop, we
    won't increase the complexity.

"""


def uncompress(s: str) -> str:
    numbers = "0123456789"
    i = 0
    j = 0
    result = []
    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    return "".join(result)
