"""
逆波兰表达式求值：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
    平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
    该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
"""
from typing import List
import re

def poland_expression(tokens: List[str]) -> int:
    stack = []
    operator = ["+", "-", "*", "/"]
    for s in tokens:
        if re.match(r"^-?\d*$", s):
            print("append\n")
            stack.append(s)
        if s in operator:
            print(stack)
            right = stack.pop()
            left = stack.pop()
            if s == '+':
                stack.append(int(right) + int(left))
            elif s == '-':
                stack.append(int(right) - int(left))
            elif s == '*':
                stack.append(int(right) * int(left))
            elif s == '/':
                stack.append(int(left)/int(right))
    return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(poland_expression(tokens))
