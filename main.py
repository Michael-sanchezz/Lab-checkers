import checkers as ch
import numpy
def game():
    size = input("what is the size of the board? ")
    print(ch.build_board(size))
    return ""

if __name__ == "__main__":
    print("in the main file")
print(game())
