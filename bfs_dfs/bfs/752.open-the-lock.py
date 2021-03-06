"""
打开转盘锁:
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

"""


class Solution:
    def openLock(self, deadends, target):
        """
        最短路径问题，BFS
        转盘数字之间的关系可以表示成图：起点是‘0000’，每个点与8个点相邻（每一位可以+1 or -1）
        """
        deadends = set(deadends)  # in 操作在set中时间复杂度为O(1)
        if target in deadends or '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        from collections import deque
        q = deque()
        q.append(['0000', 0])
        visited = set()  # 不重复遍历
        visited.add('0000')
        while q:
            val, step = q.popleft()  # 当前节点值，转动步数
            for bit in range(4):
                for add in [1, -1]:
                    new = val[:bit] + str((int(val[bit]) + add + 10) % 10) + val[bit + 1:]
                    if new == target:
                        return step + 1
                    if new not in visited and new not in deadends:
                        q.append([new, step + 1])
                        visited.add(new)

        return -1


if __name__ == '__main__':
    s = Solution()
    result = s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
    print(result)
    deadends = ["3218", "3413", "1938", "7247", "2646", "2229", "0481", "2086", "6370", "1290", "6843", "8789", "4631",
                "5060", "7412", "9415", "9048", "5514", "6940", "4311", "3775", "5562", "0576", "7141", "0438", "2154",
                "1030", "3302", "4088", "0989", "3080", "7511", "1301", "5060", "7575", "4392", "8611", "8634", "1047",
                "2396", "3810", "0601", "5603", "7164", "7011", "5119", "9843", "5168", "6306", "2070", "3440", "9344",
                "8363", "6034", "1140", "4963", "7808", "2410", "6958", "3620", "3195", "6821", "9557", "6299", "4945",
                "0813", "9311", "0279", "1938", "9531", "3732", "5111", "1130", "0806", "9289", "5868", "3481", "1074",
                "6549", "2158", "1272", "3468", "7085", "6968", "9989", "2632", "7961", "1388", "7869", "7176", "7783",
                "9186", "9803", "8710", "5420", "3894", "9026", "5212", "9258", "0017", "7571", "9735", "5901", "0051",
                "5585", "2954", "2671", "3434", "5459", "5581", "1453", "0628", "8489", "6739", "0748", "6127", "3098",
                "4988", "0300", "9497", "2041", "7155", "9567", "0630", "3504", "7043", "5552", "6217", "1849", "8770",
                "3266", "5319", "4006", "0354", "3315", "1710", "5113", "6009", "0110", "1270", "1956", "1101", "7429",
                "8610", "7221", "5032", "5375", "9657", "0196", "3351", "5274", "0918", "7865", "1477", "5806", "5433",
                "9090", "3436", "8040", "3540", "7681", "0672", "7324", "5481", "8796", "8646", "9530", "3548", "8546",
                "4339", "9710", "9646", "1902", "0707", "2259", "6943", "7604", "9083", "5806", "8984", "8182", "3504",
                "8387", "3158", "4520", "2372", "1929", "7307", "0414", "0893", "4608", "7785", "4112", "1205", "2808",
                "0767", "9701", "0370", "2765", "0567", "3450", "7802", "1738", "2558", "6041", "3789", "2075", "7614",
                "4259", "6184", "2087", "6600", "4981", "0223", "8006", "2285", "8157", "7461", "2728", "7781", "7978",
                "0323", "3828", "8350", "9345", "9164", "9241", "8775", "1353", "8404", "6706", "5744", "1722", "0945",
                "3058", "5390", "3196", "3940", "5558", "7628", "9812", "1011", "1387", "7251", "1692", "4620", "0141",
                "2641", "5644", "7022", "2622", "1290", "2981", "1777", "6245", "9138", "5243", "5253", "9080", "0701",
                "6767", "7009", "3275", "9454", "2901", "7703", "5593", "5796", "8950", "0686", "5068", "5031", "4280",
                "8907", "0467", "1424", "8715", "9337", "9732", "8259", "9624", "5039", "0027", "0245", "6051", "5384",
                "0468", "7090", "8633", "8132", "7837", "8454", "9303", "2458", "5893", "4805", "6630", "3517", "1028",
                "1885", "6894", "5958", "3220", "7512", "1869", "2174", "1198", "9420", "0939", "7390", "5749", "7915",
                "1015", "8555", "3857", "3888", "6256", "3675", "4424", "3630", "1902", "2545", "0797", "2956", "1789",
                "4829", "7030", "2091", "2574", "9368", "9005", "3452", "0143", "1223", "0172", "7594", "3750", "7802",
                "3804", "3937", "6717", "1962", "6304", "3637", "2809", "5160", "1650", "3245", "7141", "0683", "2760",
                "3650", "3883", "3734", "1858", "5569", "4351", "5565", "4973", "9045", "6874", "6087", "9420", "1393",
                "2204", "4192", "5574", "0718", "0796", "1838", "0501", "5980", "1789", "3869", "4678", "4575", "7427",
                "7540", "5527", "2547", "5110", "6515", "1448", "0286", "6344", "7237", "7770", "1462", "2356", "3076",
                "2373", "3672", "4017", "0687", "3153", "8156", "7415", "0810", "9280", "1141", "7384", "2764", "6585",
                "4668", "3738", "1526", "1489", "5830", "1450", "3323", "4717", "5708", "1324", "6739", "9005", "1191",
                "3383", "0638", "2308", "3396", "1919", "5292", "5209", "0126", "4777", "6354", "7316", "0940", "5592",
                "2099", "4870", "2543", "2228", "0640", "2394", "7973", "1131", "5453", "5048", "3732", "1597", "3527",
                "0348", "0072", "9640", "5976", "9749", "5579", "9799", "7407", "8861", "2088", "6553", "9087", "2156",
                "0948", "5973", "0047", "2287", "8979", "4867", "5707", "9414", "3774", "0051", "8570", "5113", "0875",
                "3625", "1592", "7231", "9373", "3731", "7941", "4937", "6683", "4436", "8247", "6852", "3780", "3703",
                "1453", "3211", "5679", "6100", "7588", "5414", "1887", "6074", "8944", "9473", "3737", "5895", "8275",
                "7345", "8009", "7053", "3008", "2418", "3417"]
    target = "8232"
    result = s.openLock(deadends, target)
    print(result)
