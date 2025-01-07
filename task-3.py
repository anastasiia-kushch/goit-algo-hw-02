
def is_symmetric(expression):

    """
    Checks whether the given expression contains symmetric delimiters 
    (round, square, or curly brackets).

    Args:
        expression (str): The input string containing brackets and other characters.

    Returns:
        None: Prints a message indicating whether the expression is symmetric or not.

    The function works by using a stack to store opening brackets. 
    When a closing bracket is encountered, it checks if the most recent 
    opening bracket matches it. If any mismatch or unbalanced brackets 
    are found, the expression is considered not symmetric. The function 
    is case-sensitive and ignores all characters that are not brackets.
    """
    
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in expression:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack: 
                print(f"The expression \"{expression}\" isn't symmetric.")
                return
            if char != pairs[stack.pop()]:
                print(f"The expression \"{expression}\" isn't symmetric.")
                return
        
    if stack:
        print(f"The expression \"{expression}\" isn't symmetric.")
        return
    else:
        print(f"The expression \"{expression}\" is symmetric.")
        return

is_symmetric(')(({({})}))(')