#  number of digits in N = log10(N) + 1.
from math import log,floor

def getDigits(N):
    k = floor(log(N,10) + 1)
    return k



if __name__ == "__main__":

    print("Number of digits : ",getDigits(int(input("Enter your number : "))))
