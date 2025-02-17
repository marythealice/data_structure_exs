def product_array_except_self(nums):
    output_array = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        output_array[i] = prefix
        prefix*= nums[i]

    postfix = 1

    for i in range(len(nums)-1, -1, -1):
        output_array[i] *= postfix
        postfix *= nums[i]
    return output_array 