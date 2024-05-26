from Queue import Queue


class HuffmanEncoder:

    def encode(self, original_s:str, include_capital_letters:bool):
        if include_capital_letters:
            s = original_s
        else:
            s = original_s.lower()
        occurences = self.get_letter_dict(s)
        q = self.get_letter_queue(occurences)

        pass
    def get_letter_dict(self, s):
        return {x:s.count(x) for x in s}
    def get_letter_queue(self, occurences:dict):
        q = Queue()
        for k, v in occurences.items():
            q.enqueue_raw(k, v)
        print(q)
        return q