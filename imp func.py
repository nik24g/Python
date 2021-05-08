def cin(*args):
    print(*args, end="")
    val = input()
    return val


if __name__ == '__main__':
    a = int(cin())
    print(a + 1)
