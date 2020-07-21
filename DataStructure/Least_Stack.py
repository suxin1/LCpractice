
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = [float["inf"]]

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]