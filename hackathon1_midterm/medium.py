#1
def anagram_number(number):
    string1 = str(number)
    string2 = ''.join(reversed(string1))
    number1 = int(string2)
    if number == number1:
        return True
    else:
        return False
#print(anagram_number(1254))
#print(anagram_number(121121))

#2
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val = int_val+ rom_val[s[i]] - 2*rom_val[s[i - 1]]
            else:
                int_val = int_val + rom_val[s[i]]
        return int_val