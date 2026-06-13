class MinStack:

    def __init__(self):
        self.stack  = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            min_cur = min(val,self.stack[-1][1])
            self.stack.append((val,min_cur))
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        
