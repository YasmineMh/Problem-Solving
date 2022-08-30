import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    ts_set = set(ts)

    if len(ts) > 0:
        minTemp = ts[0]
    else:
        minTemp = 0

    for i in ts:
        if abs(i) < abs(minTemp):
            minTemp = i

    if minTemp < 0:
        reverse = minTemp - minTemp * 2
        if reverse in ts_set:
            minTemp = reverse

    return minTemp


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    # n = int(input())
    ts = [15, -7, 9, 14, 7, 12]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()
