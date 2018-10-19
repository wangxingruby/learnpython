# 找出最大最小
def findMaxMin(lis):
    maxindex = 0
    minindex = 0
    for i in range(0,len(lis),1):
        if lis[i] > lis[maxindex]:
            maxindex = i
        if lis[i] < lis[minindex]:
            minindex = i
    lis[0],lis[maxindex] = lis[maxindex],lis[0]
    lis[-1],lis[minindex] = lis[minindex],lis[-1]
    print(lis)

#findMaxMin([76,34,98,76,234,9876,123456,65,23,98,76,2,1234])


def findPerfectNbr(maxrange):
    for i in range(1,maxrange,1):
        sum = 0
        for j in range(1,i,1):
            if i%j == 0:
                sum += j
        if sum == i:
            print(sum)

findPerfectNbr(1000)