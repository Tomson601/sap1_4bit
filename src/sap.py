# Computer parts: ALU, Register, Clock,

# ALU class:

class ALU:
    def __init__(self, bits=4):
        self.bits = bits

    def add(self, a, b):
        if len(a) > self.bits or len(b) > self.bits:
            return print("Error: data overflow")
        else:
            result = [0, 0, 0, 0]
            carry = 0
            a.reverse()
            b.reverse()
            for i in range(self.bits):
                if carry == 1:
                    result[i] += 1
                if a[i] + b[i] == 2:
                    carry = 1
                else:
                    result[i] = a[i] + b[i]
            result.reverse()
            return result, carry

ALU = ALU()

a = [0,1,1,0]
b = [0,1,1,0]

print(ALU.add(a, b))
