a,b=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(a)]
s=sum([sum(i) for i in mat])
print(s)
