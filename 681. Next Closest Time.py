class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [time[0],time[1],time[3],time[4]]
        result=time
        minDifference = 24*60
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if  "00" <=digits[i]+digits[j] <"24" and "00" <=digits[k]+digits[l] <"60":
                            new_time = digits[i]+digits[j]+":"+digits[k]+digits[l]
                            new_time_diff = self.time_diff(time,new_time)
                            if new_time_diff < minDifference:
                                minDifference = new_time_diff
                                result = new_time
        return result        
        
    def time_diff(self,t1,t2):
        m1=int(t1.split(":")[0])*60 + int(t1.split(":")[1])
        m2=int(t2.split(":")[0])*60 + int(t2.split(":")[1])
        if m1<m2:
            return m2-m1
        else:
            return 24*60 - (m1-m2)
        
print(Solution().nextClosestTime("00:00"))
print(Solution().nextClosestTime("19:34"))