class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                pointer = 0
                while pointer!=slow:
                    pointer = nums[pointer]
                    slow = nums[slow]
                return pointer