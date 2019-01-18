seq=int(input())
mr,mi=map(int,input().split())
lst=[[i for i in input()] for i in range(seq)]
pr,pi=[i for i in range(seq) if "p" in lst[i]][0],[i.index("p") for i in lst if "p" in i][0]
if pr==mr:
    print("LEFT" if pi<mi else "RIGHT")

else:
    def upanddown(lst,ups=[],):
        for i in lst:
            if "m" in i:m=i.index("m");break
            ups.append(i)
        return ups,lst[["m" in i for i in lst].index(True)+1:]
    up,down=upanddown(lst)
    ppos=lambda :"DOWN" if any(["p" in i for i in down]) else "UP" #if any(["p" in i for i in up]) else "mid"
    moves=[]
    [moves.append(ppos()) for i in range(abs(mr-pr))]
    [moves.append("LEFT" if pi<mi else "RIGHT") for i in range(abs(mi-pi))]
    print(moves[0])