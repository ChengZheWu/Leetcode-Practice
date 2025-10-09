# https://leetcode.com/problems/min-stack/description/
'''
1. Stack

T: All functions are O(1)
S: O(n)
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[-1]:
            self.min_val = val
        self.stack.append(val)
        self.stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()
        if not self.stack:
            self.min_val = float('inf')
        else:
            self.min_val = self.stack[-1]

    def top(self) -> int:
        temp_min = self.stack.pop()
        top_val = self.stack[-1]
        self.stack.append(temp_min)
        return top_val

    def getMin(self) -> int:
        return self.stack[-1]
    
'''
2. Stack

Use two stack, one is for nums, another is for min value

T: All functions are O(1)
S: O(n)
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]