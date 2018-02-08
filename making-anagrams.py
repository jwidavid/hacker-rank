# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
def number_needed(a, b):
    count = 0
    # ASCII code 97 = a, code 123 = z
    for ascii_code in range(97, 123):
        letter = chr(ascii_code)
        count += abs(a.count(letter) - b.count(letter))
    return count
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
