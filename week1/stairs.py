import sys

steps_number = int(sys.argv[1])

for step_width in range(1, steps_number + 1):
    row_text = ""
    for column in range(steps_number, 0, -1):
        if step_width >= column:
            row_text += "#"
        else:
            row_text += " "

    print(row_text)


"""
 print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
"""

"""
for row in range(1, steps_number + 1):
    row_text = ""
    for column in range(steps_number, 0, -1):
        step_width = row
        if column <= step_width:
            row_text += "#"
        else:
            row_text += " "

    print(row_text)
"""

