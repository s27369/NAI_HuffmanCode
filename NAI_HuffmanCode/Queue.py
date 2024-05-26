
class Node:
    def __init__(self, s:str, num:int):
        self.s=s
        self.num=num
        self.next=None

    def add_next(self, node):
        self.next=node
    def get_next(self):
        return self.next
    def get_num(self):
        return self.num
    def get_s(self):
        return self.s

class Queue:
    def __init__(self):
        self.head=None
    def set_head(self, node):
        self.head = node
    # def get_last(self):
    #     if self.head is None:
    #         return None
    #     current = self.head
    #     while current.get_next() is not None:
    #         current = current.get_next()
    #     return current

    def replace_head(self, node):
        curr_head = self.head
        node.next = curr_head
        self.head = node
    def enqueue(self, node):
        if self.head is None:
            self.head = node
            return
        if self.head.get_num()>node.get_num():
            self.replace_head(node)
        elif self.head.get_num()==node.get_num():
            if self.head.get_s()>node.get_s():
                self.replace_head(node)
        else:

            current = self.head

            while current.get_next() is not None:
                next = current.get_next()
                if (
                        next.get_num() > node.get_num()
                        or
                        (next.get_num() == node.get_num() and next.get_s() > node.get_s())
                ):
                    current.next = node
                    node.next=next
                    return

            current.next = node

    def enqueue_raw(self, s:str, num:int):
        self.enqueue(Node(s, num))