def binary_search(whitelist, inputdata):
    """
    在whitelist中寻找inputdata，如果存在就返回索引，不存在就返回-1
    """
    lo = 0
    hi = len(whitelist) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if inputdata > whitelist[mid]:
            lo = mid + 1
        elif inputdata < whitelist[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    whitelist = [1, 10, 20, 3, 8, 100]
    whitelist.sort()
    while True:
        inputdata = int(input("input number :"))
        result = binary_search(whitelist, inputdata)
        if result < 0:
            print(inputdata)
        if inputdata == 'stop':
            break
