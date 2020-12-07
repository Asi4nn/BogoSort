from time import time
from random import randint


def shuffle(lst):
    for i in range(0, len(lst)):
        ind = randint(0, len(lst) - 1)
        lst[i], lst[ind] = lst[ind], lst[i]


def is_sorted(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


def main():
    iter = 0
    start_time = time()

    lst = [randint(-1000000, 1000000) for i in range(10)]

    while not is_sorted(lst):
        iter += 1
        shuffle(lst)
        if iter % 1000000 == 0:
            print("Current iteration:", iter)

    print("List size:", len(lst))
    print("List:", lst)
    print("Time elapsed:", time() - start_time, "seconds")
    print("Total iterations:", iter)


main()
