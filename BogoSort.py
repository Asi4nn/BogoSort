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

    lst = [randint(-1000000, 1000000) for i in range(8)]

    while not is_sorted(lst):
        iter += 1
        shuffle(lst)
        if iter % 1000000 == 0:
            print("Current iteration:", iter)

    log = ("List size: " + str(len(lst)) + "\n" +
          "List: " + str(lst) + "\n" +
          "Time elapsed: " + str(time() - start_time) + " seconds\n" +
          "Total iterations: " + str(iter) + "\n\n")

    print(log)

    f = open("runtimes.txt", "a+")
    f.write(log)
    f.close()

main()
