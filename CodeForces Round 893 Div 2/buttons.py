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


def buttons(button):
    a, b, c = button
    if c%2 == 0:
        if a<=b:
            return False
        else:
            return True
    else:
        if b<=a:
            return True
        else:
            return False
    return

def main():
    test_cases = inp()
    for i in range(test_cases):
        button = inlt()
        temp = buttons(button)
        if temp:
            print("First")
        else:
            print("Second")
    return

main()