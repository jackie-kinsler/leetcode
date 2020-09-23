# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         test_lst = nums.copy()
        
#         for num in nums: 
#             test_num = test_lst.pop()
#             test_set = set(test_lst)
#             remainder = target - test_num
#             if remainder in test_set: 
#                 break
        
#         if remainder != test_num: 
#             return sorted([nums.index(test_num), nums.index(remainder)])
        
#         else: 
#             value1 = nums.index(test_num)
#             nums.pop(value1)
#             value2 = nums.index(remainder) + 1
#             return sorted([value1, value2])


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        test_lst = nums.copy()
        
        for num in nums: 
            test_num = test_lst.pop()
            test_set = set(test_lst)
            remainder = target - test_num
            if remainder in test_set: 
                break
        
        if remainder != test_num: 
            return sorted([nums.index(test_num), nums.index(remainder)])
        
        else: 
            value1 = nums.index(test_num)
            nums.pop(value1)
            value2 = nums.index(remainder) + 1
            return sorted([value1, value2])