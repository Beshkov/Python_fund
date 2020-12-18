# def Legendarium(element):
#     if element  == "shards":
#         return "Shadowmourne"
#     elif element == "fragments":
#         return "Valanyr"
#     elif element == "motes":
#         return "Dragonwrath"
# line = input().lower().split()

legendary = {"shards": 0, "fragments": 0, "motes": 0}

bad_leggos = {}

junk = {}

value = 0

pls_break = False
while True:
    line = input().lower().split()

    for el in line:
        if el.isdigit():
            value = int(el)

        elif el in legendary:
            legendary[el] += value

        else:
            if el not in junk:
                junk[el] = value
            else:
                junk[el] += value

        if legendary["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary["shards"] -= 250
            pls_break = True
            break
        if legendary["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary["fragments"] -= 250
            pls_break = True
            break
        if legendary["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary["motes"] -= 250
            pls_break = True
            break
    if pls_break:
        break




bad_leggos = dict(sorted(legendary.items(), key=lambda x: (-x[1], x[0])))


for mats, quant in bad_leggos.items():
    print(f"{mats}: {quant}")

junk = dict(sorted(junk.items(), key=lambda x: x[0]))
for jnk, coin in junk.items():
    print(f"{jnk}: {coin}")
