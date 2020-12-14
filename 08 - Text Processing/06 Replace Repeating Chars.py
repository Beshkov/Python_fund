line = input()

single_letters_list = []
repeatable = ""

for el in line:

    if not el == repeatable:
        single_letters_list.append(el)
        repeatable = el
print("".join(single_letters_list))