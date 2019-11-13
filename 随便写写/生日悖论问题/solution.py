#问题是：n个人中至少有两个人生日相同的概率
#如果要求至少两个人生日相同的概率的话，反命题就是没有一个人生日是相同的
#可以先求出所有人生日都不相同的概率，然后用一减去这个概率，就得到了至少两个人生日相同的概率
#概率是连乘的形式,prob是两个人生日不同的概率，1-prob是没有一个人生日相同，所以需要每一次乘上一个1-prob就形成了连乘的形式
days = 365
numPeople = 1
prob = 0
while numPeople < 23:
    numPeople+=1
    prob = 1 - ((1-prob)*(days-(numPeople - 1))/ days)
    
    print("Number of people:",numPeople)
    print("Prob. of same birthday:",prob)
