import sys
import collections
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


def walkway(benches, cookieSellors, d, pos):
    cookieMap = collections.defaultdict(list) #cookies -> list of sellors
    minCookie = sys.maxsize
    cookies = 0
    lastCookieEaten = 0
    cookieSellorIndex = 0
    currentIndex = 0
    while currentIndex < benches:
        if cookieSellorIndex > cookieSellors or (cookieSellorIndex < cookieSellors and pos[cookieSellorIndex] > currentIndex + d):
            currentIndex += d
            cookies += 1
            lastCookieEaten = currentIndex
        elif cookieSellorIndex < cookieSellors:
            currentIndex = pos[cookieSellorIndex]
            calcCookie = skipCookieSellor(cookies, cookieSellorIndex+1, lastCookieEaten,currentIndex, benches, d, pos,cookieSellors)
            cookieMap[calcCookie].append(cookieSellorIndex)
            minCookie = min(minCookie, calcCookie)
            cookies += 1
            lastCookieEaten = pos[cookieSellorIndex]
            cookieSellorIndex += 1

    return minCookie, len(cookieMap[minCookie])

def skipCookieSellor(cookies, cookieSellorIndex,lastCookieEaten,currentIndex,benches,d,pos,cookieSellors):
    if currentIndex == 0:
        cookies += 1
    if currentIndex-lastCookieEaten >= d:
        cookies += 1
        lastCookieEaten = currentIndex

    while currentIndex < benches:

        # case: check for next cookie sellor
        if cookieSellorIndex > cookieSellors or (cookieSellorIndex < cookieSellors and pos[cookieSellorIndex] > currentIndex + d):
            currentIndex += d
            cookies += 1
            lastCookieEaten = currentIndex
        elif cookieSellorIndex < cookieSellors:
            cookies += 1
            lastCookieEaten = pos[cookieSellorIndex]
            currentIndex = pos[cookieSellorIndex]
            cookieSellorIndex += 1
    return cookies


def main():
    test_cases = inp()
    for i in range(test_cases):
        numbers = inlt()
        benches, cookieSellors, d = numbers
        pos = inlt()
        c,n = walkway(benches, cookieSellors, d, pos)
        print(c, end=" ")
        print(n)
    return

main()