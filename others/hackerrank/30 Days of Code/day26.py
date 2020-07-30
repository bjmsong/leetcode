import sys


def input():
    return sys.stdin.readline()


actual = input().strip().split(" ")  # date actually returned
expected = input().strip().split(" ")  # date expected to be returned

day0, month0, year0 = [int(item) for item in actual]
day1, month1, year1 = [int(item) for item in expected]

if year0 > year1:
    print(10000)
elif year0 == year1 and month0 > month1:
    print(500 * (month0 - month1))
elif year0 == year1 and month0 == month1 and day0 > day1:
    print(15 * (day0 - day1))
else:
    print(0)
