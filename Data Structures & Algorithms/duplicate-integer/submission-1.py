class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        heapset = set()
        for n in nums:
            if n in heapset:
                return True
            heapset.add(n) 
        return False       