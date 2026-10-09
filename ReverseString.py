text = "Manish"
result = ""

for char in range(len(text) - 1, -1, -1):
    result += text[char]

print(result)
