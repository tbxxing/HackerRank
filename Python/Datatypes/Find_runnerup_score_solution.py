if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    newList = []
    for i in arr:
        if i not in newList:
            newList.append(i)

    newList.sort(reverse=True)
    print(newList[1])
