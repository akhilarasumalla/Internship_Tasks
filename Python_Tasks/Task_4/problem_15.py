N=int(input())
d={}
for i in range(N):
    word=input()
    d[word]=d.get(word,0)+1
print(len(d))
print(*d.values())
