# palindrome

from collections import deque

def is_palindrome(string: str) -> None:
    """
    Determines whether the given string is a palindrome.
    
    The function is case-insensitive and ignores spaces.
    
    Parameters:
        string (str): The input string to be checked.
    
    Returns:
        None: Prints a message indicating whether the string is a palindrome.
    """
    deque_string = deque(string.lower().replace(" ", ""))

    while len(deque_string) > 1:
        if deque_string.pop() != deque_string.popleft():
            print(f"The string \"{string}\" isn't a palindrome.")
            return

    print(f"The string \"{string}\" is a palindrome.")
    return
    

is_palindrome("awa wawa")