class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        duplicate_elemets_arr = []
        dist_arr =[]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if(arr[i]==arr[j]):
                    duplicate_elemets_arr.append(arr[i])
        for num in arr:
            if num not in duplicate_elemets_arr:
                dist_arr.append(num)
        if len(dist_arr)>k-1:
            return dist_arr[k-1]
        return ""