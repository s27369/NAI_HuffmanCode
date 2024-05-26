from HuffmanEncoder import HuffmanEncoder


def interface(he:HuffmanEncoder):

    while r := int(input("1 - enter string\n2 - quit\n>>>")):
        if r=="1":
            r = input("string to code>>>")
            he.encode(r)
        elif r=="2":
            quit(0)
        else:
            print("Incorrect input")



if __name__ == '__main__':
    print("Huffman code project - s27369\n")

    he = HuffmanEncoder()
    interface(he)