str1 = "dfa12321afd"


def second_highest(str):
    unique = set()
    for ele in str:
        if ele.isdigit():
            unique.add(int(ele))
    unique = sorted(unique, reverse=True)
    if len(unique) < 2:
        return -1
    return unique[1]


print(second_highest(str1))
