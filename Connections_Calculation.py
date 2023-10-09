import numpy as np


def calculate_connections(Barge_Matrix):
    Connections_Matrix = np.zeros((len(Barge_Matrix), len(Barge_Matrix[0])))
    for i in range(len(Barge_Matrix)):
        for j in range(len(Barge_Matrix[0])):
            count = 0
            if i >= 1 and j >= 1:
                if i < (len(Barge_Matrix) - 1) and j < (len(Barge_Matrix[0]) - 1):
                    if Barge_Matrix[i][j] != 0:
                        if Barge_Matrix[i - 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i + 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j + 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i + 1][j + 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j + 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i + 1][j - 1] != 0:
                            count = count + 1
                        Connections_Matrix[i][j] = count
                    Connections_Matrix[i][j] = count
                if i == (len(Barge_Matrix) - 1) and j < (len(Barge_Matrix[0]) - 1):
                    if Barge_Matrix[i][j] != 0:
                        if Barge_Matrix[i - 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j + 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j + 1] != 0:
                            count = count + 1
                        Connections_Matrix[i][j] = count
                if i < (len(Barge_Matrix) - 1) and j == (len(Barge_Matrix[0]) - 1):
                    if Barge_Matrix[i][j] != 0:
                        if Barge_Matrix[i - 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i + 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i + 1][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j - 1] != 0:
                            count = count + 1
                        Connections_Matrix[i][j] = count
                if i == (len(Barge_Matrix) - 1) and j == (len(Barge_Matrix[0]) - 1):
                    if Barge_Matrix[i][j] != 0:
                        if Barge_Matrix[i - 1][j] != 0:
                            count = count + 1
                        if Barge_Matrix[i][j - 1] != 0:
                            count = count + 1
                        if Barge_Matrix[i - 1][j - 1] != 0:
                            count = count + 1
                        Connections_Matrix[i][j] = count
            if i == 0 and 0 < j < (len(Barge_Matrix[0]) - 1):
                count += 3
                if Barge_Matrix[i][j] != 0:
                    if Barge_Matrix[i + 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j - 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j + 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i + 1][j - 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i + 1][j + 1] != 0:
                        count = count + 1
                    Connections_Matrix[i][j] = count
            if i == 0 and j == 0:
                count += 3
                if Barge_Matrix[i][j] != 0:
                    if Barge_Matrix[i + 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j + 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i + 1][j + 1] != 0:
                        count = count + 1
                    Connections_Matrix[i][j] = count
            if 0 < i < (len(Barge_Matrix) - 1) and j == 0:
                if Barge_Matrix[i][j] != 0:
                    if Barge_Matrix[i + 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j + 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i + 1][j + 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i - 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i - 1][j + 1] != 0:
                        count = count + 1
                    Connections_Matrix[i][j] = count
            if i == (len(Barge_Matrix) - 1) and j == 0:
                if Barge_Matrix[i][j] != 0:
                    if Barge_Matrix[i - 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j + 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i - 1][j + 1] != 0:
                        count = count + 1
                    Connections_Matrix[i][j] = count
            if i == 0 and j == (len(Barge_Matrix[0]) - 1):
                count += 3
                if Barge_Matrix[i][j] != 0:
                    if Barge_Matrix[i + 1][j] != 0:
                        count = count + 1
                    if Barge_Matrix[i][j - 1] != 0:
                        count = count + 1
                    if Barge_Matrix[i + 1][j - 1] != 0:
                        count = count + 1
                    Connections_Matrix[i][j] = count

    return Connections_Matrix
