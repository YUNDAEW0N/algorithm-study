import sys
input=sys.stdin.readline



N=input().split('-')
print(N)
result=0

for i in N[0].split('+'):
    result+=int(i)
    print(N)
    print(result)


for i in N[1:]:
    for j in i.split('+'):
        result-=int(j)


print(result)
