def twoSum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[i], i]
        numMap[nums[i]] = i
    
    return []
        

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, i))
