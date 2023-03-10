# Computer parts: ALU, Register, Clock,
# Data can be only loaded from bus.

class ALU:
    def __init__(self, bits=4):
        self.bits = bits

    def _add(self, a, b):
        if len(a) > self.bits or len(b) > self.bits:
            return print("Error: data overflow")
        else:
            result = [0 for i in range(self.bits)]
            carry = 0

            a.reverse()
            b.reverse()

            for i in range(self.bits):
                if carry == 0:
                    if a[i] + b[i] < 2:
                        result[i] = a[i] + b[i]
                    else:
                        carry = 1
                else:
                    if a[i] + b[i] + carry == 3:
                        result[i] = 1
                        carry = 1

                    elif a[i] + b[i] + carry == 2:
                        result[i] = 0
                        carry = 1

                    elif a[i] + b[i] + carry == 1:
                        result[i] = 1
                        carry = 0

            result.reverse()
            return result, carry

    def _load_a(bus, a):
        if type(bus) != "<class '__main__.BUS'>":
            return("Data can be only loaded from the bus")
        else:
            return a

    def _load_b(bus, b):
        if type(bus) != "<class '__main__.BUS'>":
            return("Data can be only loaded from the bus")
        else:
            return b

    def _out():
        pass


class BUS:
    def __init__(self, bits=4):
        self.bits = bits

    def _data(self, data):
        pass

    def _load(bus, data):
        if type(bus) != "<class '__main__.BUS'>":
            return("Data can be only loaded from the bus")
        else:
            return data

    def _out(self, data):
        pass


class REGISTER:
    def __init__(self, bits=4):
        self.bits = bits

    def _out(self, data_out):
        pass

    def _load(bus, data):
        if type(bus) != "<class '__main__.BUS'>":
            return("Data can be only loaded from the bus")

    def _stored_data(self, data):
        pass

bus = BUS()

bus._load()
# print(type(bus), type(bus2))
