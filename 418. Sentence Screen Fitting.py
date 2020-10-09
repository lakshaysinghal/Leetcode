from math import floor
class Solution:
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        newSentence = ' '.join(sentence) + ' '
        ptr = 0
        n = len(newSentence)
        for i in range(rows):
            ptr+=cols-1
            if newSentence[ptr%n].isspace():
                ptr+=1
            elif newSentence[(ptr+1)%n].isspace():
                ptr+=2
            else:
                while ptr>0 and not newSentence[(ptr-1)%n].isspace():
                    ptr-=1
        return floor(ptr/n)
        
print(Solution().wordsTyping(["hello", "world"],2,8))
print(Solution().wordsTyping(["a", "bcd", "e"],3,6))
print(Solution().wordsTyping(["I", "had", "apple", "pie"],4,5))
print(Solution().wordsTyping([" "],4,5))