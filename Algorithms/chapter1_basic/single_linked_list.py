"""
链表特点：
- 节省空间：不需要连续空间，不需要分配多余空间
- 增加数据：快
- 删除数据：快
- 查找数据：慢

下面介绍链表的常见操作
"""


# 创建链表
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


last = Node("or")
mid = Node("be", last)
head = Node("to", mid)

# 从表头删除结点
head = head.next

# 在表头插入结点
oldfirst = head
head = Node("not", oldfirst)

# 在表尾插入结点 -- last结点已知
oldlast = last
newlast = Node("not")
oldlast.next = newlast

# 在表尾插入结点 -- last结点未知
newNode = Node("not")
if not head:
    head = newNode
else:
    probe = head
    while probe.next:
        probe = probe.next
    probe.next = newNode

# 从表尾删除结点
if not head.next:
    head = None
else:
    probe = head
    while probe.next.next:
        probe = probe.next
    probe.next = None


# 用循环创建链表,并访问链表
head = None
for count in range(1, 6):
    head = Node(count, head)
probe = head
while probe:
    print(probe.data)
    probe = probe.next

# 搜索
targetItem = 3
probe = head
while probe and targetItem != probe.data:
    probe = probe.next
if probe:
    print("target is found")
else:
    print("target is not in this linked structure")

# 访问链表的第i项
probe = head
index = 3
while index > 0:
    probe = probe.next
    index -= 1
print(probe.data)

# 替换：若目标项不存在，则返回False；否则替换相应的项，并返回True.
probe = head
newItem = 30
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    probe.data = newItem
    print("True")
else:
    print("False")

# 在任意位置插入
if not head or index <= 0:
    head = Node(newItem, head)
else:
    probe = head
while index > 1 and probe.next:
    probe = probe.next
    index -= 1
    probe.next = Node(newItem, probe.next)

# 在任意位置删除
if index <= 0 or not head.next:
    head = head.next
else:
    probe = head
while index > 1 and probe.next.next:
    probe = probe.next
    index -= 1
    probe.next = probe.next.next
