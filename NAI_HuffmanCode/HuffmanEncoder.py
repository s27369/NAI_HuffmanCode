from MyQueue import *


class HuffmanEncoder:

    def encode(self, original_s:str, include_capital_letters:bool=False):
        s = original_s if include_capital_letters else original_s.lower()
        occurences = self.get_letter_dict(s)
        q = self.get_letter_queue(occurences)

        while q.has_2_more():
            first, second = q.dequeue(), q.dequeue()
            new_node = first.join_with_older(second)
            q.enqueue(new_node)

        codes = {}
        root = q.dequeue()
        self.generate_codes(root, "", codes)
        print(f"Original string: {original_s}")
        print(f"Encoded string: {self.get_encoded_str(s, codes)}")
        print(f"Codes: {codes}")
        # return codes

    def get_encoded_str(self, s:str, codes:dict):
        result = str()
        for char in s:
            result+=codes[char]
        return result

    def get_letter_dict(self, s):
        return {x:s.count(x) for x in s}
    def get_letter_queue(self, occurences:dict):
        q = MyQueue()
        for k, v in occurences.items():
            q.enqueue_raw(k, v)
        # print(q)
        return q
    def generate_codes(self, node:Node, current_code:str, codes:dict):
        # base case (stops recursion)
        if node is None:
            return
        # check if node is leaf node (no children)
        if not node.left_child and not node.right_child:
            # for char in node.get_s():
            #     codes[char] = current_code
            codes[node.get_s()] = current_code
            return
        # recursively traverse the tree
        self.generate_codes(node.left_child, current_code+"0", codes)
        self.generate_codes(node.right_child, current_code+"1", codes)