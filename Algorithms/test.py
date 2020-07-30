def combinationSum(candidates, target):
    # DFS
    # case： candidates:[2,2,3,5], target:8
    def search(candidates, target, index, temp, result):
        # 搜索candidates后面的值能否加到result中
        if target < 0:  # 路径错误
            return
        elif target == 0:  # 搜索完毕
            new_temp = temp.copy()  # temp的改动会影响result！
            result.append(new_temp)
            return
        for i in range(index, len(candidates)):  # target>0 继续搜索, index是之前搜索的位置
            if target < candidates[i]:
                break
            temp.append(candidates[i])
            search(candidates, target - candidates[i], i, temp, result)  # 通过DFS搜索下一个元素
            temp.pop(len(temp) - 1)  # 搜索完毕，将最新值去除，然后尝试下一个元素

    result = []
    temp = []  # 存储中间结果
    candidates.sort()
    search(candidates, target, 0, temp, result)
    return result


if __name__ == '__main__':
    solution = combinationSum([2, 3, 5], 8)
    print(solution)
