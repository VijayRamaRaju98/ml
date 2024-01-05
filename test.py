from typing import List

class Solution:
    def containsduplicate(self, nums:List[int])-> bool:
        n = nums.sort()
        for i in range(1, len(nums)):
            if n[i]==[n[i-1]]:
                print(nums)
                return True
                break
        else:
            return False


nums = [2,3,5,6,2]

c = Solution()
print(c.containsduplicate(nums=nums))