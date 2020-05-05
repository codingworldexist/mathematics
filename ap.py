"""
General Formulas to solve problems related to Arithmetic Progressions:

If ‘a’ is the first term and ‘d’ is the common difference:
nth term of an AP = a + (n-1)*d.

Arithmetic Mean = Sum of all terms in the AP / Number of terms in the AP.
Sum of ‘n’ terms of an AP = 0.5 n (first term + last term) = 0.5 n [ 2a + (n-1) d ].

"""


class ap:

    def __init__(self,a,d):
        """a is the first term
            d is the common difference
        """
        self.a = a
        self.d = d
    def getTerm(self,n):
        term = self.a + (n-1)* self.d
        return term

    def getAM(self,AP):
        """AP : list containing elements of AP"""

        AM = sum(AP)/len(AP)
        return AM
    def sumOfNTerms(self,n):
        """
        n : nth term till which sum is required
        0.5 n [ 2a + (n-1) d ]
        """
        S = 0.5*n*(2 *self.a + (n-1)*self.d)
        return S

if __name__ =="__main__":

    AP = ap(2,2)
    print("Third term is : ",AP.getTerm(3))
    print("AM OF AP{} is {} ".format([2,4,6,8],AP.getAM([2,4,6,8])))
    print("Sum of first 10 terms : ",AP.sumOfNTerms(10))




    






