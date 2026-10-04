class Solution:
    def candy(self, ratings: List[int]) -> int:
        tot=1
        i=1
        n=len(ratings)
        while i<n:
            #flat
            if ratings[i]==ratings[i-1]:
                tot+=1
                i+=1
                continue
            peak=1
            while i<n and ratings[i-1]<ratings[i]:
                peak+=1
                tot+=peak
                i+=1
            down=1
            while i<n and ratings[i-1]>ratings[i]:
                tot+=down
                down+=1
                i+=1
            if peak<down:
                tot+=(down-peak)
        return tot