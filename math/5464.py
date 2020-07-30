class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottle = 0
        sum_bottles = 0
        while numBottles > 0:
            sum_bottles += numBottles
            empty_bottle += numBottles
            numBottles = empty_bottle // numExchange
            empty_bottle -= numExchange * numBottles
        return sum_bottles


if __name__ == '__main__':
    s = Solution()
    assert (s.numWaterBottles(15, 4) == 19)
    assert (s.numWaterBottles(5, 5) == 6)
    assert (s.numWaterBottles(2, 3) == 2)
    assert (s.numWaterBottles(9, 3) == 13)
