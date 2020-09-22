
def check_grades(string):
    grades = intify_grades(string)
    return_strings_arr = []

    green_count = count_greens(grades)
    amber_count = count_ambers(grades)
    red_count = count_reds(grades)

    if green_count > 0:
        return_strings_arr.append(f"Green: {green_count}")
    if amber_count > 0:
        return_strings_arr.append(f"Amber: {amber_count}")
    if red_count > 0:
        return_strings_arr.append(f"Red: {red_count}")

    seprator = "\n"
    return seprator.join(return_strings_arr)


def intify_grades(string):
    words = string.split(", ")
    return [int(word) for word in words]


def count_greens(arr):
    return sum(i >= 75 for i in arr)


def count_ambers(arr):
    return sum(i in range(50, 75) for i in arr)


def count_reds(arr):
    return sum(i < 50 for i in arr)
