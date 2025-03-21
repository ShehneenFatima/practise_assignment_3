#Implement a function that meets the specification below. Use a try-except block.
#def sumDigits(s):
#"""Assumes s is a string
#Returns the sum of the decimal digits in s
#For example, if s is 'a2b3c' it returns 5"""
def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s.
    For example, if s is 'a2b3c' it returns 5.
    """
    total = 0
    for char in s:
        try:
            total += int(char)  # Try converting character to integer
        except ValueError:
            pass  # Ignore non-numeric characters
    return total

# Example Usage:
print(sumDigits('a2b3c'))  # Output: 5
print(sumDigits('hello123'))  # Output: 6
print(sumDigits('abc'))  # Output: 0
print(sumDigits('99bottles'))  # Output: 18
