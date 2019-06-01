def towerofhanoi(n,a,b,c):
    print("n : ",n)
    if n==1:
        print(a,c)
        return
    towerofhanoi(n-1,a,c,b)
    print(a,c)
    towerofhanoi(n-1,b,a,c)

n=int(input())
towerofhanoi(n, 's', 'h', 'd')
