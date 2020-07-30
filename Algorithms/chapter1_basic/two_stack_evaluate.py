"""
双栈实现算数表达式求值
1. 将操作数压入操作数栈
2. 将运算符压入运算符栈
3. 忽略左括号
4. 遇到右括号，弹出运算符，弹出所需数量的操作数，并将运算符和操作数的运算结果压入操作数栈
"""

if __name__ == '__main__':
    ops = list()
    vals = list()
    s = input("请输入算数表达式，字符之间用空格隔开,例如 ( 1 + 11 ):")
    s_split = s.split(" ")
    for i in range(len(s_split)):
        c = s_split[i]
        if c == "(":
            pass
        elif c in ("+", "-", "*", "/"):
            ops.append(c)
        elif c == ")":
            op = ops.pop()
            val = vals.pop()
            if op == "+":
                v = val + vals.pop()
            elif op == "-" :
                v = vals.pop() - val
            elif op == "*" :
                v = val * vals.pop()
            elif op == "/":
                v = vals.pop() / val
            vals.append(v)
        else:
            vals.append(int(c))
    print(vals.pop())
