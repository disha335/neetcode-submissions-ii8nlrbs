class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0]*26
        max_count = 0
        hf = 0

        for task in tasks:
            indexTask = ord(task[0])-ord('A')
            counter[indexTask]+=1
            if counter[indexTask]==hf:
                max_count+=1
            elif counter[indexTask]>hf:
                hf = counter[indexTask]
                max_count = 1

        parts = hf-1
        slotsPerPart = n-(max_count-1)
        es = slotsPerPart*parts
        t = len(tasks)-max_count*hf
        idles = max(es-t, 0)

        return idles+len(tasks)