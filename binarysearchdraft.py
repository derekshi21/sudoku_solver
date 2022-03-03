from fileinput import close
import time
import random
import timeit


def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1
    
    midpoint = (high + low) // 2
    
    if list[midpoint] == target:
        return midpoint
    elif target > list[midpoint]:
        return binary_search(list, target, midpoint+1, high)
    else:
        return binary_search(list, target, low, midpoint-1)
        

if __name__ == "__main__":
    length = 9999
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    sorted_list_search = open("sorted_list_search.txt", "w")
    for n in sorted_list:
        sorted_list_search.write(str(int(n)) + " \n")
    sorted_list_search.close

    target = random.choice(sorted_list)
    
    print(str(int(naive_search(sorted_list, target))) + " index")
    print(str(int(binary_search(sorted_list, target))) + " index")
    print(target, " is the randomly generated target.")

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, " seconds.")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, " seconds.")