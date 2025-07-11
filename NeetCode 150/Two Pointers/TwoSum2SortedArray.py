def twosum2(nums, target): # Remember, nums is sorted
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left+1, right+1]

if __name__ == "__main__":
    print(twosum2([1, 2, 3, 4], 3))