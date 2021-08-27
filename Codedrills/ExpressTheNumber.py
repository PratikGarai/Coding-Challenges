# https://codedrills.io/contests/icpc-amritapuri-2020-preliminary-round/problems/express-the-number

t = int(input())

for i in range(t):
	
	n,x = map(int, input().split())
	k = 0
	
	if n % 2 != 0 and x == 0:
		print(-1)
		continue
	
	while(n>x):
		s = 2
		while((s*4)<=n):
			s *= 4
		n -= s
		k += 1
	
	if n==0:
		print(k)
	else :
		print(k+1)
