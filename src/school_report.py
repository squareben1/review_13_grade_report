
def grade_checker(string):
    words = string.split(", ")
    grades = [int(word) for word in words]

    green_count = 0
    amber_count = 0
    red_count = 0

    for i in grades:
        if i < 75 and i >= 50:
            amber_count += 1
        elif i >= 75:
            green_count += 1
        elif i < 50:
            red_count += 1

    print(amber_count)
    if green_count > 0:
        return f"Green: {green_count}"
    elif amber_count > 0:
        return f"Amber: {amber_count}"
    elif red_count > 0:
        return f"Red: {red_count}"
