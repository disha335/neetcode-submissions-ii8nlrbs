class StockSpanner:

    def __init__(self):
        self.st=[]
        self.i=0

    def next(self, price: int) -> int:
        while self.st and self.st[-1][1]<=price:
            self.st.pop()
        ans=self.i-self.st[-1][0] if self.st else self.i+1
        self.st.append((self.i,price))
        self.i+=1
        return ans
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)