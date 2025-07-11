def pascal(nums):

    def reducelist(numbers):
        return [numbers[i-1]%10 + numbers[i]%10 for i in range(1, len(numbers))]
    
    while True:
        if len(nums) == 2:
            return str(nums[0]%10) + str(nums[1]%10)
        nums = reducelist(nums)

if __name__ == "__main__":
    print(pascal([4, 5, 6, 7]))