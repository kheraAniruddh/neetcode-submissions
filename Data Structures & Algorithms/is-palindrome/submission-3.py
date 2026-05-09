class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        input =""
        for c in s:
            if c.isalnum():
                input +=c
        print(input)
        rev = input[::-1] 
        return input == rev     
        