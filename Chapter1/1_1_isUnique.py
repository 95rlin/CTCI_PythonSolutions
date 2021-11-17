from collections import Counter


def is_unique(arg):
    # input = abcdeeee
    # result = false
    cnt = Counter(arg)
    for i in cnt.values():
        if i > 1:
            return False
    return True


# Runtime = n + n == O(n)
def is_unique2(arg):
    return len(set(arg)) == len(arg)

# Runtime = O(n)


if __name__ == '__main__':
    print(is_unique("abcde"))
    print(is_unique2("abcde"))
