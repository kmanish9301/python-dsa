numbers = [1,1,2,3,4,5,5,4,3,1]
occur ={}

def find_occur(numbers):

    for num in numbers:
        if num not in occur:
            occur[num] = 1
        else:
            occur[num] += 1

find_occur(numbers)
