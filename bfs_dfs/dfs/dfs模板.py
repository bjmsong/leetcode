def dfs(cur, target, visited):
    """
    模板1: 递归
    使用的是由系统提供的隐式栈，也称为调用栈（Call Stack）
    优点： 容易实现
    缺点：如果递归的深度太高，将遭受堆栈溢出
        - 解决方案：BFS，或使用显式栈实现DFS
    """
    if cur == target:
        return True
    for next in cur.neighbors:
        if next not in visited:
            visited.add(next)
            if dfs(next, target, visited):
                return True

    return False


# boolean DFS(int root, int target) {
#     Set<Node> visited;
#     Stack<Node> s;
#     add root to s;
#     while (s is not empty) {
#         Node cur = the top element in s;
#         return true if cur is target;
#         for (Node next : the neighbors of cur) {
#             if (next is not in visited) {
#                 add next to s;
#                 add next to visited;
#             }
#         }
#         remove cur from s;
#     }
#     return false;
# }


def dfs(root, target):
    """
    模板2：显式栈实现DFS
    该逻辑与递归解决方案完全相同。 但使用while循环和栈来模拟递归期间的系统调用栈
    跟BFS的写法类似,区别在于BFS使用queue，DFS使用stack
    """
    stack = []
    visited = set()
    stack.append(root)
    while stack:
        node = stack.pop()
        if node == target:
            return True
        for next in node.neighbors:
            if next not in visited:
                visited.add(next)
                stack.append(next)
    return False
