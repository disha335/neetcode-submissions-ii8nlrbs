class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        taken = set()

        def dfs(crs):
            if crs in taken:
                return False
            if preMap[crs] == []:
                return True
            
            taken.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            taken.remove(crs)
            preMap[crs] = []  # Mark the course as checked by emptying its prerequisites list
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return False
                
        return True