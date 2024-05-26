class Node:
    def __init__(self, s: str, num: int):
        self.s = s
        self.num = num
        self.next = None #for queue
        self.left_child = None #for binary tree
        self.right_child = None #for binary tree


    def join_with_older(self, older_node):
        n = Node(self.get_s() + older_node.get_s(), self.get_num() + older_node.get_num())
        n.left_child = self
        n.right_child = older_node
        return n

    def comes_after(self, node):
        return (
                self.get_num() > node.get_num()
                or
                (self.get_num() == node.get_num() and self.get_s() > node.get_s())
        )

    def add_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def get_num(self):
        return self.num

    def get_s(self):
        return self.s


class MyQueue:
    def __init__(self):
        self.head = None

    def set_head(self, node):
        self.head = node

    def has_2_more(self):
        if self.head is not None:
            return self.head.get_next() is not None
        return False

    def replace_head(self, node):
        curr_head = self.head
        node.next = curr_head
        self.head = node

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            return
        if self.head.comes_after(node):
            self.replace_head(node)
        else:
            current = self.head
            while current.get_next() is not None:
                next = current.get_next()
                if next.comes_after(node):
                    current.next = node
                    node.next = next
                    return
                current=next
            current.next = node

    def enqueue_raw(self, s: str, num: int):
        self.enqueue(Node(s, num))

    def dequeue(self) -> Node:
        if self.head is None: return None
        result = self.head
        self.head = self.head.get_next()
        return result
