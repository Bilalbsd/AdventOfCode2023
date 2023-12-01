f = open("./src/day01/data.txt", "r")
values = f.read().split()

#print(values)

result = 0

for value in values:
    result_str = ""
    for elem in value:
        if elem in "0123456789":
            result_str += elem

    if len(result_str) >= 2:
        result += int(result_str[0] + result_str[-1])
    if len(result_str) == 1:
        result += int(result_str[0] * 2)

print(result)