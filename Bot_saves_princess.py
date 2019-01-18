seq=int(input())
lst=[[i for i in input()] for i in range(seq)]
bot=["m" in i for i in lst].index(True)
mr,pr=[i for i in range(seq) if "m" in lst[i]][0],[i for i in range(seq) if "p" in lst[i]][0]
mi,pi=[i.index("m") for i in lst if "m" in i][0],[i.index("p") for i in lst if "p" in i][0]
def upanddown(lst,ups=[],):
    for i in lst:
        if "m" in i:
            m=i.index("m")
            break
        ups.append(i)
    return ups,lst[bot+1:]
up,down=upanddown(lst)
ppos=lambda :"DOWN" if any(["p" in i for i in down]) else "UP" #if any(["p" in i for i in up]) else "mid"
moves=[]
[moves.append(ppos()) for i in range(abs(mr-pr))]
[moves.append("LEFT" if pi<mi else "RIGHT") for i in range(abs(mi-pi))]
for i in moves:print(i)