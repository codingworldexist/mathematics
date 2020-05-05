"""
Therefore, we can say that:
10K-1 <= N < 10K
Applying base-10 logarithm to both sides in the above equation, we get:
K-1 <= log10(N) < K.

or, K - 1 + 1 <= log10(N) + 1 < K + 1
or, K <= log10(N) + 1 < K + 1
Therefore,
K = floor(log10(N) + 1)

"""



#  number of digits in N = log10(N) + 1.
from math import log,floor

def getDigits(N):
    k = floor(log(N,10) + 1)
    return k



if __name__ == "__main__":

    print("Number of digits : ",getDigits(int(input("Enter your number : "))))
