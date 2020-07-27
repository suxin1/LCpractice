"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
"""


def is_valid(s: str) -> bool:
    
    valid_char = ' '
    start = '([{'
    end = ')]}'
    stack = []
    for char in s:
        if char in valid_char:
            continue
        if char in start:
            stack.append(char)
        elif char in end:
            if not len(stack):
                return False
            token = end.index(char)
            prev_char = stack.pop()
            if prev_char == start[token]:
                continue
            return False
    if len(stack) > 0:
        return False
    return True


print(is_valid('((){})'))
