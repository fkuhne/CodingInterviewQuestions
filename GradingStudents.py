# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

import math

def differenceForNextMultipleOf5(value):
    if value%5 == 0: return 0
    else: return 5 - value%5

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38: continue
        d = differenceForNextMultipleOf5(grades[i])
        if d < 3: grades[i] += d
    return grades

grades = [4, 73, 67, 38, 33]

print(gradingStudents(grades))

# print("73 / 5 = {}".format(73/5))
# print("73 % 5 = {}".format(73%5))

# print("73 / 10 = {}".format(round(73/10,1)))

# print("73 / 10 = {}".format(round(73/10,1)))