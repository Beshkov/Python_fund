def avr_grade_generator(val):
    return sum(val)/len(val)


number = int(input())

teh_grand_dict = {}

for i in range(number):
    student = input()
    grade = float(input())

    if student not in teh_grand_dict:

        teh_grand_dict[student] = []

    teh_grand_dict[student].append(grade)

teh_grand_dict = {key: avr_grade_generator(val) for (key, val) in teh_grand_dict.items() if avr_grade_generator(val) >= 4.5}

avr_grades = dict(sorted(teh_grand_dict.items(),key= lambda x: x[1], reverse=True))

for el, a_grades in avr_grades.items():
    print(f"{el} -> {a_grades:.2f}")