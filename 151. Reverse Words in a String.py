class Solution:
    def reverseWords(self, s: str) -> str:
        clean=s.split()
        clean=clean[::-1]
        return " ".join(clean)
