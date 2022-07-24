def findDuplicate(nums) -> int:
    maps = {}
    for i in nums:
        try:
            maps[i] += 1
            print("Executed try", maps)
            return i
        except KeyError:
            maps[i] = 1


print(findDuplicate([3, 1, 3, 4, 2]))
