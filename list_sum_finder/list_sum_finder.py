class Solution:
    def __init__(self):
        self.lst = []

    def two_sum(self, target, nums):
        for i in range(len(nums)):
            for k in range(len(nums)):
                sum_ = nums[i] + nums[k]
                if i != k and sum_ == target:
                    self.lst.append(i)

        return self.lst
