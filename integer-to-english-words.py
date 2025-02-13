"""

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:
0 <= num <= 231 - 1


Time Complexity: O(N), where N is the number of digits in the input (at most 10 for a 32-bit integer).
Space Complexity: O(N) due to the recursive function calls and storing the word representation.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# 1. divide the number into groups of three digits (thousands, millions, billions) and process each separately.
# 2. A helper function converts each three-digit chunk into words using mappings for ones, teens, and tens.
# 3. concatenate the converted chunks with the appropriate place values and return the final string.


class Solution:
  
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        ones_map = {
                        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
                        15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 
                        19: "Nineteen"
                    }

        tens_map = {
                        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 
                        60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
                    }

        
        def helper(n):
            
            res = []
            hundreds = n // 100

            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            
            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                res.append(tens_map[10 * tens])
                if ones:
                    res.append(ones_map[ones])
            elif last_2:
                res.append(ones_map[last_2])

            return ' '.join(res)

        postfix = ["", " Thousand", " Million", " Billion"]
        res = []
        i = 0

        while num:

            digits = num % 1000

            s = helper(digits) 
            if s:
                res.append(s + postfix[i])

            num = num // 1000
            i += 1

        res.reverse()

        return ' '.join(res)

