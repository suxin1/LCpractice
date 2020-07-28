"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
"""


def is_valid(s: str) -> bool:
    """
    声明一个堆栈N
    遍历字符串中的所有字符
        如果该字符为开括符，则将其堆叠道堆栈N
        如果该字符为闭阔符，拉出栈N中的第一个符号与其配对
            如不能配对，则这个字符串无效，返回假。反之，继续遍历。
    如堆栈N中元素个数为0，则说明字符串有效，返回真。反之，则说明字符串无效，返回假。
    :param s: string
    :return: boolean
    """
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

    return not stack


print(is_valid("((( ))){"))

