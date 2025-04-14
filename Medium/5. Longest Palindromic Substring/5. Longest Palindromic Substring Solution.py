class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2:
            return s

        longest = ""
        for i in range(len(s)):
            # Check for odd length palindromes centered at i
            palindrome1 = expand_around_center(i, i)
            # Check for even length palindromes centered between i and i+1
            palindrome2 = expand_around_center(i, i + 1)

            # Update the longest palindrome found so far
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
