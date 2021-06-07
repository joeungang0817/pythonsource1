from sys import stdin
inputed=int(stdin.readline().strip())
n=int(stdin.readline().strip())
cal=inputed-(inputed%n)
ran=cal/n
sum=0
for i in range(int(ran)):
	sum=n*(i+1)+sum
print(sum)