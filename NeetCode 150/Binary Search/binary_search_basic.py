"""
Return position of element in array if found, else return -1
"""
def binarySearch(nums, target):

    # First, sort the array
    nums = sorted(nums)
    print(f"The sorted array is: {nums}")
    # Initialize left and right pointers
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left if nums[left] == target else -1

if __name__ == "__main__":
    print(binarySearch([2, 1, -1, 2, 45, -300, -217, -400, 1, 58, 29, 48], 48))