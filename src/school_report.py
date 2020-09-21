
def grade_checker(string):
    words = string.split(", ")
    grades = [int(word) for word in words]

    green_count = 0
    amber_count = 0

    for i in grades:
        if i < 75:
            amber_count += 1
        elif i >= 75:
            green_count += 1

    if green_count > 0:
        return f"Green: {green_count}"
    else:
        return f"Amber: {amber_count}"
