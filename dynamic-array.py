n,q=[int(i) for i in input().split()]
lst,lan=[[int(i) for i in input().split()] for i in range(q)],0
seql=[[] for i in range(n)]
for i in lst:
    if i[0]==1:seql[(i[1]^lan)%n].append(i[2])
    else:
        lan=seql[(i[1]^lan)%n][i[2]%len(seql[(i[1]^lan)%n])]
        print(lan)