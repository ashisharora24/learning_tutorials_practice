# A ComplexNumber class contains two data members : one is real part (R) and other is imaginary (I) (both integer).
# Implement the Complex numbers class that contains following functions -
# 1. constructor (You need to create the appropriate constructor.)
# 2. plus - (# This function adds two given complex numbers and updates the first complex number.)
# e.g.
# if C1 = 4 + i5 and C2 = 3 +i1
# C1.plus(C2) results in:
# C1 = 7 + i6 and C2 = 3 + i1
# 3. multiply - (# This function multiplies two given complex numbers and updates the first complex number.)
# e.g.
# C1 = 4 + i5 and C2 = 1 + i2
# C1.multiply(C2) results in:
# C1 = -6 + i13 and C2 = 1 + i2
# 4. print - (# This function prints the given complex number in the following format :)
# a + ib
# Note : There is space before and after '+' (plus sign) and no space between 'i' (iota symbol) and b.
# Input Format :
# Line 1 : Two integers - real and imaginary part of 1st complex number
# Line 2 : Two integers - real and imaginary part of 2nd complex number
# Line 3 : An integer representing choice (1 or 2) (1 represents plus function will be called and 2 represents multiply function will be called)
# Sample Input 1 :
# 4 5
# 6 7
# 1
# Sample Output 1 :
# 10 + i12
# Sample Input 2 :
# 4 5
# 6 7
# 2
class Complex_Number:

    def __init__(self,real = 0,imag = 0):
        self.real = real
        self.imag = imag

    def printCN(self):
        print(self.real," + i",self.imag,sep='')


    def sum(self,otherCN):
        temp_real = self.real + otherCN.real
        temp_imag = self.imag + otherCN.imag
        self.real = temp_real
        self.imag = temp_imag
        self.printCN()

    def multiple(self,otherCN):
        temp_real = (self.real * otherCN.real) - (self.imag * otherCN.imag)
        #print(self.real * otherCN.imag)
        #print(self.imag * otherCN.real)
        #print((self.real * otherCN.imag) + (self.imag * otherCN.real))
        temp_imag = (((self.real) * (otherCN.imag)) + ((self.imag) * (otherCN.real)))
        self.real = temp_real
        self.imag = temp_imag
        self.printCN()


(real, imag) = list(int(i) for i in input().strip().split(' '))
F1 = Complex_Number(real, imag)
(real, imag) = list(int(i) for i in input().strip().split(' '))
F2 = Complex_Number(real, imag)
process = int(input().strip())
if process == 1:
    F1.sum(F2)
else:
    F1.multiple(F2)
