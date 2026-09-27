# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)

# print(stack)

# top = stack[-1]

# print(top, len(stack))

# print(stack.pop())
# print(stack)


class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.next = None


class MyStack:
    def __init__(self) -> None:

        # initially stack is empty
        self.top = None
        self.count = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.count += 1

    def pop(self):

        if self.top is None:
            print("Stack Underflow")
            return -1

        temp = self.top
        self.top = self.top.next
        val = temp.data
        self.count -= 1

        del temp
        return val

    def peek(self):

        if self.top is None:
            print("Stack is Empty")
            return -1

        return self.top.data

    def isEmpty(self):
        return self.top is None

    # size of stack
    def size(self):
        return self.count

    def print_list(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    st = MyStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print(st.print_list())
    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())
    
    s = "carcarcarcarcar"
    print(s.find('car'))
    print(s.count('car'))
    for i in range(ord('a'), ord('z') + 1):
        print(i,chr(i))