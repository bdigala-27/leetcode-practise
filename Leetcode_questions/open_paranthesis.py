'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''


def isValid(s):
    opcl = dict(('()', '[]', '{}'))
    stack = []
    for i in s:
        if i in '({[':
            stack.append(i)
        elif len(stack) == 0 or i!=opcl[stack.pop()]:
            return False
    return len(stack) == 0
s = "()[]{}"
print(isValid(s))