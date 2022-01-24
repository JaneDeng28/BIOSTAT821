def get_data(path:str) -> list:
    mydata = []
    with open(path, 'r') as file:
        for line in file:
            mydata.append(list(map(float, line.split(' '))))
    return mydata


def analyze_data(list:list, Method:str) -> float:
    numlist = []
    for i in list:
        for j in i:
            numlist.append(j)

    if Method == "average":
        print(sum(numlist)/ len(numlist))

    if Method == "standard deviation":
        mean = sum(numlist) / len(numlist)
        print((sum([(x - mean)**2 for x in numlist])/len(numlist))**0.5)

    if Method == "covariance":
        mean_0 = sum(list[0]) / len(list[0])
        mean_1 = sum(list[1]) / len(list[1])
        sub_0 = [i - mean_0 for i in list[0]]
        sub_1 = [i - mean_1 for i in list[1]]
        numerator = sum([sub_0[i]*sub_1[i] for i in range(len(sub_0))])
        denominator = len(list[0])
        print(numerator / denominator)

    if Method == "correlation":
        mean_0 = sum(list[0]) / len(list[0])
        mean_1 = sum(list[1]) / len(list[1])
        sub_0 = [i - mean_0 for i in list[0]]
        sub_1 = [i - mean_1 for i in list[1]]
        numerator = sum([sub_0[i] * sub_1[i] for i in range(len(sub_0))])
        std_0 = sum(sub_0[i]**2 for i in range(len(sub_0)))
        std_1 = sum(sub_1[i]**2 for i in range(len(sub_1)))
        denominator = (std_0*std_1)**0.5
        print(numerator / denominator)
