import itertools
arrlen,lines=map(int,input().split())
arr=[0]*(arrlen+1)
for i in range(lines):
    start,end,num=map(int,input().split())
    arr[start-1]+=num;arr[end]-=num
print(max(itertools.accumulate(arr)))