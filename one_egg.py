#CODEVITA 2017 ROUND 2 D PROBLEM
M, X = map(int , input().split(" "))
li = []
#add = 0
for i in range(M):
    li.append(int(input()))
    #add = add + li[i]
N = sum(li)
if N >= X:
    print("Thank you, your order for 150 eggs are accepted")
else:
    print("Sorry, we can only supply "+str(N-1)+" eggs")
    X = X - abs(X-N) - 1
cst = X
for i in range(M):
    cst = cst - li[i]
    if cst >= 0:
        print("{0}    {1}    {2}".format(li[i],li[i],0))
    elif (li[i] - cst) > 0:
        cst = cst + li[i]
        print("{0}    {1}    {2}".format(li[i],cst,li[i]-cst))
        cst = 0
    else:
        print("{0}    {1}    {2}".format(li[i],cst,li[i]))
