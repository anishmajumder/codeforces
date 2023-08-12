import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def gameWithArrays(arrays):
    # print(arrays)
    smallest_first = sys.maxsize
    smallest_second = sys.maxsize
    arr = []
    for array in arrays:
        array.sort()
        smallest_first = min(smallest_first,array.pop(0))
        smallest_second = min(smallest_second, array[0])
        if array[0] == smallest_second:
            arr = array
    # print(smallest_first)
    # print(smallest_second)
    # print(arr)
    arr.append(smallest_first)
    arr.sort()
    # print(arrays)

    sum = 0

    for array in arrays:
        sum += array[0]

    return sum

def main():
    test_cases = inp()
    for i in range(test_cases):
        num_Arrays = inp()
        arrays = []
        for j in range(num_Arrays):
            arr_len = inp()
            arr = inlt()
            arrays.append(arr)
        print(gameWithArrays(arrays))
    return

main()