str1, str2 = input().split()

one = len(str1)
two = len(str2)

summer_time_sadness = 0

if one > two:
    for i in range(two):
        summer_time_sadness += ord(str1[i]) * ord(str2[i])
    for j in range(1,(one - two)+1):
        summer_time_sadness += ord(str1[-j])
elif one < two:
    for i in range(one):
        summer_time_sadness += ord(str1[i]) * ord(str2[i])
    for j in range(1,(two - one)+1):
        summer_time_sadness += ord(str2[-j])

else:
    for i in range(one):
        summer_time_sadness += ord(str1[i]) * ord(str2[i])

print(summer_time_sadness)