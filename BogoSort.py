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


def main(size, tests, file_name):
    avg_time = 0
    avg_iter = 0

    for i in range(tests):
        iter = 0
        start_time = time()

        lst = [randint(-1000000, 1000000) for i in range(size)]

        while not is_sorted(lst):
            iter += 1
            shuffle(lst)
            if iter % 1000000 == 0:
                print("Current iteration:", iter)

        end_time = time()

        avg_time += end_time - start_time
        avg_iter += iter

        # log = ("List size: " + str(len(lst)) + "\n" +
        #       "List: " + str(lst) + "\n" +
        #       "Time elapsed: " + str(end_time - start_time) + " seconds\n" +
        #       "Total iterations: " + str(iter) + "\n\n")
        #
        # print(log)
        #
        # f = open(file_name, "a+")
        # f.write(log)
        # f.close()

    avg_time = avg_time / tests
    avg_iter = round(avg_iter / tests)
    total_log = ("List size: " + str(len(lst)) + "\n" +
                "Number of tests: " + str(tests) + "\n" +
                "Average time elapsed: " + str(avg_time) + " seconds\n" +
                "Average iterations: " + str(avg_iter) + "\n\n")

    print(total_log)

    f = open(file_name, "a+")
    f.write(total_log)
    f.close()


main(9, 100, "runtimes.txt")
