n = int(input())


x,y,z, = 0,0,0

for i in range(n):
    a,b,c = map(int, input().split())
    x += a
    y += b
    z += c

if x or y or z :
    print("NO")
else :
    print("YES")
