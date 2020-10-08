def moveZeroes(nums): 
    count = 0
    for index in range(len(nums)):
        if nums[index - count] == 0:
            del nums[index - count]
            nums.append(0)
            count += 1
    return nums
print(moveZeroes([0,1,0,3,12]))




# # initial solution
# def moveZeroes(nums): 
#     for num in nums: 
#         if num == 0:
#             del nums[nums.index(0)]
#             nums.append(0)
#     return nums