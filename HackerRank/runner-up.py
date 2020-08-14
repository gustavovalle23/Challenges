if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    win = max(arr)
    while win in arr:
        arr.remove(win)
    print(max(arr))