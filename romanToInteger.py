"""
Given a roman numeral, convert it to an integer.
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
def roman_to_integer(s):
    romans={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    res=0
    for c in range(0,len(s)-1):
        if(romans[s[c]]<romans[s[c+1]]):
            res=res-romans[s[c]]
        else:
            res=res+romans[s[c]]
    res+=romans[s[len(s)-1]]
    return res

print(roman_to_integer("XVII"))

