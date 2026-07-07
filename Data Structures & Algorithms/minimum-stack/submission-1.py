class MinStack:

    def __init__(self):
        """ Initialize the MinStack. 
        """
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        """ Push val onto stack. 
        """
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        """ Remove element from top of stack. 
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """ Get top element from stack. 
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """ Get minimum value in the stack. 
        """
        return self.min_stack[-1]
