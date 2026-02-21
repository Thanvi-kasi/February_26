class Solution:
    def reverseWords(self, s: str) -> str:
        # split() automatically removes extra spaces
        words = s.split()
        
        # reverse the list
        words.reverse()
        
        # join with single space
        return " ".join(words)
