"""

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 
Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

Time Complexity:
- Method 1 (without stack): O(N), where N is the length of the string, as each character is processed once.
- Method 2 (using stack): O(N), since each number is pushed and popped from the stack at most once.

Space Complexity:
- Method 1: O(1), as it only uses a few integer variables.
- Method 2: O(N), as it uses a stack that can store all numbers in the worst case.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# This approach evaluates a mathematical expression given as a string. 
# It processes numbers and operators sequentially using a stack to handle multiplication and division before addition and subtraction. 
# The final result is computed by summing up the values in the stack.


class Solution:

    def calculate(self, s: str) -> int:
      
        # Method 1: Using a running calculation with a tail variable
      
        if not s:
            return 0
        num = 0
        calc = 0
        tail = 0
        lastSign = '+'

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            
            if (not c.isdigit() and c != " ") or (i == len(s) - 1):
                if lastSign == '+':
                    calc += num
                    tail = num
                elif lastSign == '-':
                    calc -= num
                    tail = -num
                elif lastSign == '*':
                    calc = calc - tail + tail * num
                    tail *= num
                elif lastSign == '/':
                    calc = calc - tail + int(tail / num)
                    tail = int(tail / num)

                lastSign = c
                num = 0
            
        return calc

    # Method 2: Using a stack
  
    def calculate_stack(self, s: str) -> int:
        if not s:
            return 0
        num = 0
        calc = 0
        lastSign = '+'
        stack = []
        
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            
            if (not c.isdigit() and c != " ") or (i == len(s) - 1):
                if lastSign == '+':
                    stack.append(num)
                elif lastSign == '-':
                    stack.append(-num)
                elif lastSign == '*':
                    stack.append(stack.pop() * num)
                elif lastSign == '/':
                    stack.append(int(stack.pop() / num))

                lastSign = c
                num = 0
        
        while stack:
            calc += stack.pop()   
        return calc
