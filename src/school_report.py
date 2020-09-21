
def grade_checker(string):
    words = string.split(", ")
    grades = [int(word) for word in words]
    return_string = []

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

    if green_count > 0:
        return_string.append(f"Green: {green_count}")
    if amber_count > 0:
        return_string.append(f"Amber: {amber_count}")
    if red_count > 0:
        return_string.append(f"Red: {red_count}")

    seprator = "\n"
    print(return_string)
    return seprator.join(return_string)
