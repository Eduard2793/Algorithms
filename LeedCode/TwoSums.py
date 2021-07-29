
nums = list(map(int,input().split()))
target = int(input())


class Solution:
    def twoSum(self, nums, target):
        
        targ_minus_left = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in targ_minus_left:
                targ_minus_left[diff].append(i)
            else:
                targ_minus_left[diff] = [i]

        for i in range(len(nums)):
            if nums[i] in targ_minus_left:
                indices = targ_minus_left[nums[i]]
                for j in range(len(indices)):
                    if indices[j] < i:
                        return [indices[j],i]
   

sol = Solution()

print(sol.twoSum(nums,target))
