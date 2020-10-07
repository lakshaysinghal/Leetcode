class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b=='':
            return 0
        if len(b)==1:
            return 1 if b in a else -1
        lps = [0 for i in range(len(b))]
        
        i,j=1,0
        while i<len(b):
            if b[i]==b[j]:
                lps[i]=j+1
                i+=1
                j+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    lps[i]=0
                    i+=1
                
        c,i,j=1,0,0
        while(i<len(a)+len(b)):
            if j==len(b):
                return (i-1)//len(a) + 1
            if a[i%len(a)]==b[j]:
                i+=1
                j+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
            
        return -1

print(Solution().repeatedStringMatch("aa","aa"))
print(Solution().repeatedStringMatch("abcd","cda"))
print(Solution().repeatedStringMatch("abcd","cdabcdab"))
print(Solution().repeatedStringMatch("aaac","aac"))