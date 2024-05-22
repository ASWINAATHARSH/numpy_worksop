def is_palindrome(number):
  
    numstr = str(number)
    
    
    return numstr == numstr[::-1]


number = 12321
if ispalindrome(number):
    print(" is a palindrome.")
else:
    print(" is not a palindrome.")
