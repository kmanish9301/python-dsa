words = ["bella", "label", "roller"]

def find_common_letter(arr):
    all_frequency = []

    for word in arr:
        frequency = {}
        for letter in word:
            frequency[letter] = frequency.get(letter, 0) + 1
        all_frequency.append(frequency)

    result = []
    for letter in all_frequency[0]:
        min_count = float("inf")

        for frequency in all_frequency:
            min_count = min(min_count, frequency.get(letter, 0))

        while min_count> 0:
            result.append(letter)
            min_count -= 1

    return result

print(find_common_letter(words))
