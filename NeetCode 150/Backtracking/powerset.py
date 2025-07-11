"""
Should return all possible subsets of a given input list
"""
def powerset(nums):
    result = []
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i+1)

        subset.pop()
        dfs(i+1)

    dfs(0)
    return result


if __name__ == "__main__":
    print(powerset([1, 2, 3]))