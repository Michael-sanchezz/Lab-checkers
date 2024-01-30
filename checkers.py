from numpy import random


def build_board(size):
    x = 0
    size = int(size)
    rand = random.choice(["Empty", "Red", "Black"], (size, size))
    print(rand)
    print(get_count(size,rand))
    return ""

def get_count(board, count):
    red = (count == "Red")
    black = (count == "Black")
    empty = (count == "Empty")
    print(f"numbers of red, black, and empty in board size {board}")
    sum = (f'red {red.sum()}\nblack {black.sum()}\nempty {empty.sum()}')
    return sum

if __name__ == "__main__":
    print("not intended to be main!")
