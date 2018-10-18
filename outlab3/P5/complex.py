class Complex:
    
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag

    def __str__(self, real, imag):
        a=str('{0:g}'.format(real))
        b=str('{0:g}'.format(imag))
        if float(b)>=0:
            b='+'+b+'i'
        else:
            b=b+'i'
        print(a+b)

    def __add__(self, z1, z2):
        a=z1.real+z2.real
        b=z1.imag+z2.imag
        self.__str__(a,b)

    def __sub__(self, z1, z2):
       a=z1.real-z2.real
       b=z1.imag-z2.imag
       self.__str__(a,b)

    def __mul__(self, z1, z2):
        a=z1.real*z2.real-z1.imag*z2.imag
        b=z1.imag*z2.real+z1.real*z2.imag
        self.__str__(a,b)

    def __truediv__(self, z1, z2):
        d=float(z2.real*z2.real+z2.imag*z2.imag)
        a=(z1.real*z2.real+z1.imag*z2.imag)/d
        b=(z1.imag*z2.real-z1.real*z2.imag)/d
        self.__str__(a,b)

file=open('numbers.txt', 'r')
Nums=[]
for i in file.read().split():
    Nums.append(float (i))
    
a=Nums[0]
b=Nums[1]
c=Nums[2]
d=Nums[3]

z1=Complex(a,b)
z2=Complex(c,d)

z1.__str__(z1.real, z1.imag)
z2.__str__(z2.real, z2.imag)
z1.__add__(z1,z2)
z1.__sub__(z1,z2)
z1.__mul__(z1,z2)
z1.__truediv__(z1,z2)




        
    
