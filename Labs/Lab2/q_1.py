def geom_prob(x1, y1, x2, y2, a, b):
    if a == 0:
        if y1 <= b <= y2 or y2 <= b <= y1:
            return True
        return False

    if (y1 <= a * x1 + b <= y2) or (x1 <= (y1 - b) / a <= x2) or (
            y2 <= a * x1 + b <= y1) or (x2 <= (y1 - b) / a <= x1) or (
            y1 <= a * x2 + b <= y2) or (x1 <= (y2 - b) / a <= x2) or (
            y2 <= a * x2 + b <= y1) or (x2 <= (y2 - b) / a <= x1):
        return True
    return False


print(geom_prob(-2, -4, 2, 4, 1, 0))
print(geom_prob(-2, -4, 2, 4, 1, 0))
print(geom_prob(-2, -4, 2, 4, 0, -4))
print(geom_prob(-2, -4, 2, 4, -1, -6))


def get_largest(x1, x2, x3, y4):
    largest_num = x1
    if largest_num < x2:
        largest_num = x2
    if largest_num < x3:
        largest_num = x3
    if largest_num < y4:
        largest_num = y4
    return largest_num


print(get_largest(-2, -4, 12, 0))
