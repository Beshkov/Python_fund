password = input()
new_pass = []
for character in password:
    new_pass.append(chr(ord(character)+3))

print("".join(map(str,new_pass)))