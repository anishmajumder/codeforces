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


def unitedWeStand(A):
    B = []
    C = []

    A.sort()
    
    for a in A:
        if len(B) == 0:
            B.append(a)
            continue
        for b in B:
            if b%a == 0:
                B.append(a)
                break
        if B[-1] != a:
            C.append(a)

    return (B,C)

def main():
    test_cases = inp()
    for i in range(test_cases):
        lenA = inp()
        A = inlt()
        # print(A)
        # print(type(A))
        B, C = unitedWeStand(A)
        if len(C) == 0:
            print(-1)
        else:
            print(len(B), end = " ")
            print(len(C))
            for b in B:
                print(b, end =" ")
            print("")
            for c in C:
                print(c, end=" ")
            print("")
    return

main()