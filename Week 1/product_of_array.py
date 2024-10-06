class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre_product = 1
        post_product = 1
        result = [1] * length

        for i in range(length):
            result[i] = pre_product
            pre_product *= nums[i]
        for i in range(length-1, -1, -1):
            result[i] *= post_product
            post_product *= nums[i]
        return result