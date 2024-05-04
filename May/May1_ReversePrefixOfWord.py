class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        return word if index==-1 else word[index::-1] + word[index+1:]