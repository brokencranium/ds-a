# Create a data structure twoStacks that represents two stacks. Implementation of twoStacks
# should use only one array, i.e., both stacks should use the same array for storing elements.
# Following functions must be supported by twoStacks.

class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = data  # push to queue_stack 1

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = data  # push to queue_stack 2

    def pop1(self):
        if self.top1 >= 0:
            data = self.arr[self.top1]
            self.top1 -= 1
            return data

    def pop2(self):
        if self.top2 < self.size:
            data = self.arr[self.top2]
            self.top2 += 1
            return data

    def get_top1(self):
        if self.top1 >= 0:
            return self.arr[self.top1]

    def get_top2(self):
        if self.top2 < self.size:
            return self.arr[self.top2]

    def is_empty1(self):
        if self.top1 == -1:
            return True
        else:
            return False

    def is_empty2(self):
        if self.top2 == self.size:
            return True
        else:
            return False

    def is_full1(self):
        if self.top1 == self.size - 1:
            return True
        else:
            return False

    def is_full2(self):
        if self.top2 == 0:
            return True
        else:
            return False

    def print_stacks(self):
        print(self.arr)


# Test
if __name__ == '__main__':
    two_stacks = TwoStacks(5)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push1(3)
    two_stacks.push2(4)
    two_stacks.push2(5)

    two_stacks.print_stacks()
