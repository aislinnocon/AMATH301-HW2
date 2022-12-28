
import numpy as np

A_prep = np.zeros(646)
A = A_prep.reshape(19, 34)
for i in range(1, 20):
    for j in range(1,35):
        A[i - 1, j - 1] = 1/(i * j)
A1 = A.copy()
print(A1.shape)

B = A.copy()
B[16:17] = 0
B[:19,32:33] = 0
A2 = B
# print(A2)
print(A2.shape)

A3 = B[14:19, 31:34]
print(A3.shape)

A4 = B[:19, 4:5]
print(A4.shape)

# Problem 2


# def my_abs(x):
#     if x >= 0:
#         abs_x = x
#     else:
#         abs_x = -x
#     return abs_x


def harmonic_series(x):
    output = 0
    for k in range(1, x + 1):
        output = 1/k + output

    return output


A5 = harmonic_series(10)
print(A5)

A6 = harmonic_series(100)
print(A6)

n = 0
SN = 0
while SN <= 5:
    SN = harmonic_series(n)
    n = n + 1

A7 = n - 1
print("A7 = ")
print(A7)
A8 = SN
print(A8)


n = 1
SN = 1
f = 0
while SN <= 15:
    SN = SN + 1/(n + 1)
    n = n + 1

A9 = n
print("A9(n) = ", A9)

A10 = SN
print(A10)

# Problem 3

def model_pop(Pop, Pt, r, K):
    answer = r * Pt * (1 - (Pt / K))
    for index in range(Pop - 1):
        answer = r * answer * (1 - (answer / K))
    return answer

# ex = print(model_pop(3,3,2.5,20))
partA = np.zeros(3)
partA[0] = model_pop(998, 3, 2.5, 20)
partA[1] = model_pop(999, 3, 2.5, 20)
partA[2] = model_pop(1000, 3, 2.5, 20)

A11 = partA.reshape(1, 3)
# print(A11.shape)
# print(A11)

partB = np.zeros(3)
partB[0] = model_pop(998, 3, 3.2, 20)
partB[1] = model_pop(999, 3, 3.2, 20)
partB[2] = model_pop(1000, 3, 3.2, 20)
A12 = partB.reshape(1,3)
# print(A12)
# print(A12.shape)

partC = np.zeros(3)
partC[0] = model_pop(998, 3, 3.5, 20)
partC[1] = model_pop(999, 3, 3.5, 20)
partC[2] = model_pop(1000, 3, 3.5, 20)
A13 = partC.reshape(1,3)
# print(A13)
# print(A13.shape)





