
def grade_checker(string):
    words = string.split(", ")
    grades = [int(word) for word in words]

    green_count = len(words)
    amber_count = 0

    if grades[0] < 75:
        amber_count += 1
        return f"Amber: {amber_count}"

    return f"Green: {green_count}"
