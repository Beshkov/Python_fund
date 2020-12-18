counter = 0

resources = dict()

while True:
    counter += 1

    command = input()

    if command == "stop":
        break


    if counter % 2 == 0:
        command = int(command)
        resources[key] += command
        key = None


    else:

        key = command
        if key not in resources:
            resources[key] = 0


for el in resources:
    print(f"{el} -> {resources[el]}")