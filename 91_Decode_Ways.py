class Solution:
    numOfDecoding={}
    def numDecodings(self, s: str) -> int:
        numOfDecodingsTillPos = [0]*(len(s)+1)
        numOfDecodingsTillPos[0]=1
        
        for i in range(len(s)):
            if s[i]!='0':
                numOfDecodingsTillPos[i+1]+=numOfDecodingsTillPos[i]
            
            if i > 0 and "09"< s[i-1:i+1] <"27":
                numOfDecodingsTillPos[i+1]+=numOfDecodingsTillPos[i-1]
        return numOfDecodingsTillPos[-1]
    
'''
Time  - O(N)
Space - O(N)
'''        