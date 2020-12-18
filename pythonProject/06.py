command = input()

courses = {}

while command != "end":

    course, user = command.split(" : ")

    if course not in courses:

        courses[course] = []

    courses[course].append(user)


    command = input()


courses_pl = dict(sorted(courses.items(), key=lambda c: len(c[1]), reverse=True))

for el, val in courses_pl.items():

    print(f"{el}: {len(val)}")

    for person in sorted(val):
        print(f"--{person}")