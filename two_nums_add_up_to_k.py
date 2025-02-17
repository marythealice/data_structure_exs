def sum_nums_up_to_k(nums, k):
    set_nums = set()
    for num in nums:
        complement = k - num
        if complement in set_nums:
            return [complement, num]
        set_nums.add(num)
    return None
