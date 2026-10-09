arr = [1, 1, 2, 3, 4, 5, 1]

def remove_duplicates(nums):
    is_seen = {}
    unique_arr = []

    for num in nums:
        if num not in is_seen:
            unique_arr.append(num)
            is_seen[num] = 1

    return unique_arr, is_seen

print(remove_duplicates(arr))