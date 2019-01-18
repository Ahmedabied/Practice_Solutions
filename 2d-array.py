lst=[[int(f) for f in input().split()] for i in range(6)]
print(max([lst[i][f]+lst[i][f+1]+lst[i][f+2]+lst[i+1][f+1]+lst[i+2][f]+lst[i+2][f+1]+lst[i+2][f+2] for i in range(4) for f in range(4)]))