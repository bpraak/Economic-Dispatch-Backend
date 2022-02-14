import numpy as np

def load_dispatch(n, a, b, c, P_min, P_max, PD) :
    """
        Main function
    """
    epsilon = 0.001
    delP = 1000
    lamda = max(b)
    P = []
    while abs(delP) >= epsilon:
        P = np.divide((lamda - b), 2*a)
        P = np.minimum(P, P_max)
        P = np.maximum(P, P_min)
        
        delP = PD - np.sum(P)
        lamda = lamda + ((delP)/(np.sum(np.divide(1, 2*a))))
        
    C = np.multiply(a, np.multiply(P, P)) + np.multiply(b, P) + c
    Total_Cost = np.sum(C)
    return [P, C, Total_Cost]


# # number of generating stations
# n = 3

# # Cost = a*P^2 + b*P + c
# a = np.array([0.004, 0.006, 0.009])
# b = np.array([5.3, 5.5, 5.8]) 
# c = np.array([500.0, 400.0, 200.0])

# PD = 800 

# P_min = np.array([0, 0, 0])
# P_max = np.array([800, 800, 800])

# [P, C, Total_Cost] = load_dispatch(n, a, b, c, P_min, P_max, PD)

# print(P)
# print(C)
# print(Total_Cost)