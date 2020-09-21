
# give it a verb name, #grade_checker sounds like an object i.e. class


def check_grades(string):
    words = string.split(", ")
    grades = [int(word) for word in words]
    return_string = []

    green_count = sum(i >= 75 for i in grades)
    amber_count = sum(i >= 50 and i < 75 for i in grades)
    red_count = sum(i < 50 for i in grades)

    if green_count > 0:
        return_string.append(f"Green: {green_count}")
    if amber_count > 0:
        return_string.append(f"Amber: {amber_count}")
    if red_count > 0:
        return_string.append(f"Red: {red_count}")

    seprator = "\n"
    return seprator.join(return_string)

# commit messages:
# More descriptive, "Can count single red grades" rather than "single red"
# Lists vs. Arrays
# list - dynamic, arrays = fixed "creating an array of length 5 of int type" -
