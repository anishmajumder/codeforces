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

def anotherPerm(n):
    
    ans  = 0
    return ans

def main():
    test_cases = inp()
    for i in range(test_cases):
        print(anotherPerm(inp()))
    return

main()