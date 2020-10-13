"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
解题思路：
    把每一个字符都当成一个token，用栈来维护这些token，遍历字符串：
        1，如果字符是数字字符，将其解析为数字压入栈中。
        2，如果字符是字母或"["，直接将其压入栈中。
        3，如果字符是"]", 开始出栈，直到遇到"["。出栈序列反转后可拼接一个字符串s。取出栈顶的数字n（此时一定是数字）
    将n个s拼接为一个字符串并进栈。

    当上面的操作执行完后，栈里面就剩没有括号 [] 的字符串，将其拼接就可得到最终结果。
"""


def decode_string(s):
    stack = []
    num_temp = ""
    for token in s:
        if token == "]":
            cur_string = ""
            cur = stack.pop()
            print(stack)
            while cur != "[":
                print(stack)
                cur_string = cur + cur_string
                cur = stack.pop()
            cur_string *= stack.pop()
            stack.append(cur_string)
        elif token in "0123456789":
            num_temp += token
        else:
            if token == "[" and num_temp:
                stack.append(int(num_temp))
                num_temp = ""

            stack.append(token)
    return str.join("", stack)


print(decode_string("23[cd]ef"))
