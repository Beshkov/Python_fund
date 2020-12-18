line = input().split()
elements = {}

for el in line:
    for elem in el:
        if elem in elements:
            elements[elem] += 1
        else:
            elements[elem] = 1

for character, value in elements.items():
    print(f"{character} -> {value}")