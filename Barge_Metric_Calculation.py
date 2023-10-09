import numpy as np


def calculate_metric(Base_Matrix):
    Metric_Matrix = np.zeros((len(Base_Matrix), len(Base_Matrix[0])))
    for i in range(len(Base_Matrix)):
        for j in range(1, len(Base_Matrix[0])):
            if Base_Matrix[i][j] != 0:
                if Base_Matrix[i][j - 1] == 0:
                    Metric_Matrix[i][j] = Base_Matrix[i][j]
    for i in range(len(Base_Matrix)):
        for j in range(1, len(Base_Matrix[0])):
            if Metric_Matrix[i][j] == 0:
                if Base_Matrix[i][j] != 0:
                    total = 0
                    count = 0
                    for k in range(j, -1, -1):
                        if count >= 1:
                            break
                        if Base_Matrix[i][k] == 0:
                            for l in range(k + 1, j + 1):
                                if l == j:
                                    total += Base_Matrix[i][l] - 1
                                elif Base_Matrix[i][l - 1] != 0 and Base_Matrix[i][l + 1] != 0:
                                    total += (Base_Matrix[i][l] - 2) * 2
                                    total += 1
                                else:
                                    total += (Base_Matrix[i][l] - 1) * 2
                            if Base_Matrix[i][j - 1] != 0 and Base_Matrix[i][j + 1] != 0:
                                total += 2
                            if Base_Matrix[i][j + 1] == 0:
                                total -= 2
                            Metric_Matrix[i][j] = total + 1
                            count += 1

    return Metric_Matrix
