class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        dir=0 # 0->down; 1->up
        res=["" for x in range(numRows)]
        i=0
        j=0
        while j<len(s):
            if dir == 0:
                res[i]=res[i]+s[j]
                if i == numRows-1:
                    dir=1
                    i = (i-1)%numRows
                else:
                    i=(i+1)%numRows
            elif dir==1:
                res[i]=res[i]+s[j]
                if i==0:
                    dir=0
                    i=(i+1)%numRows
                else:
                    i=(i-1)%numRows
            j=j+1
            
        output = "".join(res)
        return output