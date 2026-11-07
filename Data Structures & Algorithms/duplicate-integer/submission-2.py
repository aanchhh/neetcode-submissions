from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for count in counts.values():
            if count >= 2:
                return True
        return False