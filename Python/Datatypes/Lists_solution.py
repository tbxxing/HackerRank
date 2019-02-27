if __name__ == '__main__':
    N = int(input())
    List = []

    for i in range(0, N):
        listToken = input().split()
        if listToken[0] == 'insert':
            List.insert(int(listToken[1]), int(listToken[2]))
        elif listToken[0] == 'print':
            print(List)
        elif listToken[0] == 'remove':
            List.remove(int(listToken[1]))
        elif listToken[0] == 'append':
            List.append(int(listToken[1]))
        elif listToken[0] == 'sort':
            List.sort()
        elif listToken[0] == 'pop':
            List.pop()
        elif listToken[0] == 'reverse':
            List.reverse()