"""

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string 
that reads the same forwards and backwards.)

"""

def check_is_palindrome(element):
    palindrome_element = element[::-1]
    return element == palindrome_element

element_to_check = input("Write a word to determine if is a palindrome: ")
print("Is a palindrome? " + str(check_is_palindrome(element_to_check)))