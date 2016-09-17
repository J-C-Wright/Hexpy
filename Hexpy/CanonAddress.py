import StandardAddress as sa
import SpiralAddress as spa

class CanonAddress(object):

    def __init__(self,address):
        assert address.isdigit() or isinstance(address,int),'Must give an integer input'
        address=str(address)
        for i in address:
            assert int(i) < 7,'Number must be in base 7'

        self.address = address

    def order(self):
        return len(self.address)

    def digits(self):
        digits = []
        for digit in self.address:
            digits.append(digit)
        return digits

    def increment(self,step=1):
        spiral_self = spa.spiralFromCanon(self)
        spiral_self.increment(step=step)
        self.address = canonFromSpiral(spiral_self).address

    def decrement(self,step=1):
        spiral_self = spa.spiralFromCanon(self)
        spiral_self.decrement(step=step)
        self.address = canonFromSpiral(spiral_self).address

    def __str__(self):
        return self.address

    def __int__(self):
        return int(self.address)

    def __add__(self,other):
        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self + standard_other)

    def __sub__(self,other):
        standard_self = sa.standardFromCanon(self)
        standard_other = sa.standardFromCanon(other)
        return canonFromStandard(standard_self - standard_other)

    def __invert__(self):
        standard_self = sa.standardFromCanon(self)
        return canonFromStandard(~standard_self)






def canonFromStandard(address):

    canonStr = ''
    for digit in address.digits():
        if digit.bin == '100':
            canonStr += '1'
        elif digit.bin == '010':
            canonStr += '2'
        elif digit.bin == '110':
            canonStr += '3'
        elif digit.bin == '001':
            canonStr += '4'
        elif digit.bin == '101':
            canonStr += '5'
        elif digit.bin == '011':
            canonStr += '6'
        else: 
            canonStr += '0'  #111 = 000
    return CanonAddress(canonStr)
        
def canonFromSpiral(spiral):

    address = int(spiral)
    length = len(str(address))
    canonStr = ''

    for i in range(length,-1,-1):
        rem = address % 7**i
        if (rem != address):
            canonStr += str((address - rem)/(7**i))
            address = rem
        else:
            canonStr += '0'
    if canonStr[0] == '0':
        return CanonAddress(canonStr[1:])
    else:
        return CanonAddress(canonStr)

   
    
    
    
