# https://codedrills.io/contests/icpc-amritapuri-2020-regional-round/problems/thanos-the-teacher 

t = int(input())

for i in range(t) :
	n = int(input())
	a = sorted(list(map(int, input().split())))
	
	last = (a[0]+a[-1])/2
	p = True
	for i in range(n):
		k = (a[i]+a[2*n-i-1])/2
		if k!=last :
			p = False
			break
	
	if p :
		print("PERFECT")
	else :
		print("IMBALANCED")
