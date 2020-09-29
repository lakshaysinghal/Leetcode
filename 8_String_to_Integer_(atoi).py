class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        sign = 1 # 1-> positive; -1-> negative
        l = len(str)
        idx = 0
        while idx < l and str[idx] == ' ':
            idx+= 1
        
        if idx<l and str[idx]=='-':
            sign=-1
            idx+=1
        elif idx<l and str[idx]=='+':
            sign=1
            idx+=1
        
        if idx == l:
            return 0
        
        if not str[idx].isnumeric():
            return 0
        
        while(idx<l and str[idx].isnumeric()):
            res=res*10
            res+=int(str[idx])
            idx+=1
        
        if res >= 2**31 and sign == 1:
            return (2**31)-1
        elif res>= 2**31 and sign == -1:
            return -1*(2**31)
        
        return res*sign
        