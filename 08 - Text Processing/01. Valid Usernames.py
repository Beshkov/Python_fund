usernames = input().split(", ")

valid_names = []

for name in usernames:
    if 3 <= len(name) <= 16:
        if "-" in name or "_" in name or name.isalnum():
            valid_names.append(name)

for el in valid_names:
    print(el)