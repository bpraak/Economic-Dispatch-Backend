import numpy as np
import random as random

# def load_dispatch(n, a, b, c, P_min, P_max, PD) :
#     """
#         Main function
#     """
#     epsilon = 0.001
#     delP = 1000
#     lamda = max(b)
#     P = []
#     while abs(delP) >= epsilon:
#         P = np.divide((lamda - b), 2*a)
#         P = np.minimum(P, P_max)
#         P = np.maximum(P, P_min)
        
#         delP = PD - np.sum(P)
#         lamda = lamda + ((delP)/(np.sum(np.divide(1, 2*a))))
        
#     C = np.multiply(a, np.multiply(P, P)) + np.multiply(b, P) + c
#     Total_Cost = np.sum(C)
#     return [P, C, Total_Cost]


def load_dispatch(n, a, b, c, P_min, P_max, PD):
    """
        Main function
    """
    vis = np.ones(n)
    P = np.zeros(n)
    while(True):
        f = 0
        x = np.sum(np.multiply(vis, np.divide(1, 2*a)))
        y = np.sum(np.multiply(vis, np.divide(b, 2*a)))
        lamda = (PD + y) / x
        for i in range(n):
            if(vis[i] == 1):
                P[i] = (lamda - b[i])/(2*a[i])
            if(vis[i] == 1 and P[i] < P_min[i]):
                P[i] = P_min[i]
                PD = PD - P_min[i]
                vis[i] = 0
                f = 1
            elif (vis[i] == 1 and P[i] > P_max[i]):
                P[i] = P_max[i]
                PD = PD - P_max[i]
                vis[i] = 0
                f = 1
        if f == 0:
            break
    C = np.multiply(a, np.multiply(P, P)) + np.multiply(b, P) + c
    Total_Cost = np.sum(C)
    return [P, C, Total_Cost]


def load_dispatch_loss(n, a, b, c, P_min, P_max, B, PD):
    epsilon = 0.001
    delP = 10
    lamda = max(b)
    P = []
    PL = 0

    while abs(delP) >= epsilon:
        P = np.divide((lamda - b), 2*a)
        diff = 10
        while diff >= epsilon:
            P1 = P
            # print(P)
            for i in range(n):
                x = 0
                for j in range(n):
                    if i!=j:
                        x = x + 2 * B[i][j] * P1[j]
                P1[i] = (1 - b[i]/lamda - x)/(2*a[i]/lamda + 2*B[i][i])
                P1[i] = min(P1[i], P_max[i])
                P1[i] = max(P1[i], P_min[i])
            diff = max(abs(P1 - P))
            P = P1
        PL = np.dot(np.transpose(P), np.dot(B, P))
        delP = PD + PL - np.sum(P)

        lamda = lamda + ((delP)/(np.sum(np.divide(1, 2*a))))

    C = np.multiply(a, np.multiply(P, P)) + np.multiply(b, P) + c
    Total_Cost = np.sum(C)

    return [P, PL, C, Total_Cost]
