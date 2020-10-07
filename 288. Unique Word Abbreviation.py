class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictAbbr = {}
        for word in dictionary:
            if len(word)<=2:
                self.dictAbbr[word]={word}
            else:
                abbr = word[0]+str(len(word)-2)+word[-1]
                if abbr in self.dictAbbr:
                    self.dictAbbr[abbr].add(word)
                else:
                    self.dictAbbr[abbr]={word}

    def isUnique(self, word: str) -> bool:
        abbr = word[0]+str(len(word)-2)+word[-1] if len(word)>2 else word
        if abbr not in self.dictAbbr:
            return True
        elif word in self.dictAbbr[abbr] and len(self.dictAbbr[abbr])==1:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)