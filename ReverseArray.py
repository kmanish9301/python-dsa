numbers = [1,2,3,4,5,6]
# Two Pointers
# left = 0
# right = len(numbers)-1
#
# while left < right:
#     numbers[left], numbers[right] = numbers[right], numbers[left]
#     left += 1
#     right -= 1
#
# print(numbers)

# Using Loop
result = []
for num in range(len(numbers)-1,-1,-1):
    result.append(numbers[num])

print(result)
