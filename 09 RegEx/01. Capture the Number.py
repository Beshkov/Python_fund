import re

while True:
    data = input().strip()

    if data == "":
        break

    pattern = r"\d+"

    val = re.findall(pattern, data)
    if val == []:
        continue

    print(" ".join(val), end=" ")