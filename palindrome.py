def is_palindrome(sub):
    return sub == sub[::-1]

def palindromic_substrings(s):
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if is_palindrome(substring):
                substrings.add(substring)
    return substrings


 # Check if the length of the input string is valid
s = input("Enter a string: ").strip()
if 1 <= len(s) <= 1000:
    palindromes = palindromic_substrings(s)
    print("Palindromic substrings:", palindromes)
else:   # Test the function
    print("String does not have a valid length")

