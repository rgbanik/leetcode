def longestSubsequence(nums):
    # First, create a set out of the numbers array for O(1) lookup
    # Creating this set takes O(n)
    lookup = set(nums)

    # Initialize a max length variable
    max_length = 0

    # Then, we make one pass over the list.
    # Check if the element is a sequence starter, meaning num-1 isn't in the set,
    # and then keep counting up and checking if the new numbers are in the set
    for num in nums:
        if not (num-1 in lookup):
            length = 0
            increment = 0
            while num + increment in lookup:
                length += 1
                increment += 1
            max_length = max(max_length, length)

    return max_length

if __name__ == "__main__":
    print(longestSubsequence([2,20,4,10,3,4,5])) # 4
    print(longestSubsequence([0,3,2,5,4,6,1,1])) # 7