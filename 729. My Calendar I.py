class event:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=self.right=None
class MyCalendar:

    def __init__(self):
        self.event = None

    def book(self, start: int, end: int) -> bool:
        if not self.event:
            self.event=event(start,end)
            return True
        return self.bookUtil(self.event,start,end)
    
    def bookUtil(self,current,start,end):
        if current.end <= start:
            if not current.right:
                current.right = event(start,end)
                return True
            else:
                return self.bookUtil(current.right,start,end)
        
        if current.start >= end:
            if not current.left:
                current.left = event(start,end)
                return True
            else:
                return self.bookUtil(current.left,start,end)
        
        return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)