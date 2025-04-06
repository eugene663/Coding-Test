def gcd(a, b):
    while b > 0:
        a, b  = b, a%b
    return a

N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))
n, m = 1,1

for i in n_nums:
    n *= i
for j in m_nums:
    m *= j

print(str(gcd(n,m))[-9:])