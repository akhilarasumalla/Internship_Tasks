n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
l=[]
s2=set(map(int,input().split()))
for i in sorted(s1-s2):
    l.append(i)
for j in sorted(s2-s1):
    l.append(j)
print(*sorted(l),sep='\n')
