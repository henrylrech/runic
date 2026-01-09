
from handlers import _roll as raw_roll
def try_roll(expr):
    try:
        raw_roll(expr)
    except Exception as e:
        msg = f"Expr: {expr}, Error: {e}"
        print(msg)

def test():
    print("testing dice rolls:")
    try_roll("d6")
    try_roll("d20")
    try_roll("2d6")
    try_roll("3d4")
    try_roll("5d10")
    try_roll("5d10 + d9")
    try_roll("1d4 / 3")
    try_roll("2d6 + 3")
    try_roll("2d6 + 3d4")
    try_roll("2d6 + 3d4 - 1d8")
    try_roll("(2d6 + 1) * 2")
    try_roll("2 * (1d8 + 2d4)")
    try_roll("2d6+3d4-1d8")
    try_roll(" 2d6 + 3d4 - 1d8 ")
    try_roll("1d1")
    try_roll("10d1")
    try_roll("1d100")
    print("all tests done.")

if __name__ == "__main__":
    test()