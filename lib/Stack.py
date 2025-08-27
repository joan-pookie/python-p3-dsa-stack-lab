class Stack:
    def __init__(self, items=None, limit=None):
        """
        Initialize a stack with optional initial items and optional limit.
        :param items: list of initial stack items
        :param limit: maximum number of elements in the stack
        """
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, value):
        """Add a value to the top of the stack. Raise OverflowError if full."""
        if self.limit is not None and len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(value)
        return self

    def pop(self):
        """Remove and return the top value. Return None if empty."""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top value without removing it. None if empty."""
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0

    def isEmpty(self):
        """Alias for empty() to match test method name."""
        return self.empty()

    def full(self):
        """Return True if stack has reached its limit, False otherwise."""
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        """
        Return the distance from the top of stack to the value.
        Top has distance 0. Return -1 if not found.
        """
        for distance, item in enumerate(reversed(self.items)):
            if item == value:
                return distance
        return -1
