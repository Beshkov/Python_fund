line = input()

for el in range(len(line)):
    if line[el] == ":":
        print(line[el:el + 2])