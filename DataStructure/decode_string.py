
def analysis(s):
    tokens = []
    num_str = ""
    sub_str = ""
    for c in s:
        if c in "0123456789":
            num_str += c
            if sub_str:
                tokens.append(sub_str)
                sub_str = ""
        elif c in "[]":
            if num_str:
                tokens.append(int(num_str))
                num_str = ""
            if sub_str:
                tokens.append(sub_str)
                sub_str = ""
            tokens.append(c)
        else:
            sub_str += c
    if sub_str:
        tokens.append(sub_str)
    return tokens


def decodeString(tokens):
    stack = []
    for index, token in enumerate(tokens):
        if token == "]":
            cur = stack.pop()
            cur_string = ""
            while cur != "[":
                cur_string = cur + cur_string
                cur = stack.pop()
            cur_string *= stack.pop()
            stack.append(cur_string)

        else:
            stack.append(token)
    return str.join("", stack)


tokens = analysis("23[cd]ef")
print(tokens)
print(decodeString(tokens))
