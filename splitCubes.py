def get_split_cubes(low, high):
    nums = []

    for num in range(low, high + 1):
        curr_sum = 0
        for split_num in list(str(num)):
            split_num = int(split_num)
            curr_sum += (split_num ** 3)
        if curr_sum == num:
            nums.append(num)
    for num in nums:
        print("{}".format(num), end=', ')


get_split_cubes(100, 1000)
