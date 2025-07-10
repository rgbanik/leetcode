def combination_sum(nums, target):
    
    result = []
    subset = []
    
    def dfs(i, numbers):
        if i >= len(numbers):
            result.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i+1, nums[i+1:])

        subset.pop()
        dfs(i+1, nums[i+1])

    dfs(0, nums)
    return result 


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))