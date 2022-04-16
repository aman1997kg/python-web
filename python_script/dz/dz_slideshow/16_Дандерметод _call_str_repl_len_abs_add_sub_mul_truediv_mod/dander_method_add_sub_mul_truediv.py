class Time:
    __time = 86400

    def __init__(self, seconds : int):
        if not isinstance(seconds, int):
            raise TypeError("Бул жерге сан жаз")
        self.seconds = seconds % self.__time

    def get_time(self):
        s = self.seconds % 60
        minutes = (self.seconds // 60) % 60
        hours = (self.seconds // 3600) % 24
        return f"{self.__check_format(hours)} : {self.__check_format(minutes)} : {self.__check_format(s)}"


    @classmethod
    def __check_format(cls, value):
        return str(value).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Time)):
            raise ArithmeticError('Сан он жактагы оперант болушу керек!')
        sc = other
        if isinstance(other, Time):
            sc = other.seconds
        return Time(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other


    def __sub__(self, other):
        if not isinstance(other, (int, Time)):
            raise ArithmeticError('Сан он жактагы оперант болушу керек!')
        sc = other
        if isinstance(other, Time):
            sc = other.seconds
        return Time(self.seconds - sc)


    def __rsub__(self, other):
        return self - other


    def __isub__(self, other):
        return self - other


    def __mul__(self, other):
        if not isinstance(other, (int, Time)):
            raise ArithmeticError('Сан он жактагы оперант болушу керек!')
        sc = other
        if isinstance(other, Time):
            sc = other.seconds
        return Time(self.seconds * sc)


    def __rmul__(self, other):
        return self * other


    def __imul__(self, other):
        return self * other


    def __truediv__(self, other):
        if not isinstance(other, (int, Time)):
            raise ArithmeticError('Сан он жактагы оперант болушу керек!')
        sc = other
        if isinstance(other, Time):
            sc = other.seconds
        return Time(self.seconds // sc)

    def __rtruediv__(self, other):
        return self / other


    def __itruediv__(self, other):
        return self / other





# truediv_time = Time(3000)
# truediv_time /= 100
# print(truediv_time.get_time())
#
# truediv_time = Time(4000000)
# truediv_time = 10000 / truediv_time
# print(truediv_time.get_time())


# mul_time = Time(20)
# mul_time *= 10
# print(mul_time.get_time())

# mul_time = Time(10)
# time2 = mul_time * 1000
# time3 = time2 * mul_time
# print(time3.get_time())
#
# mul_time = Time(20)
# time = 100 * mul_time
# print(time.get_time())




# time = Time(50)
# # time2 = Time(50)
# # time3 = 100 + time + time2
# time += 100



# time = Time(100)
# time -= 100
# print(time.get_time())

# time = Time(86400)
# print(time.get_time())

# time2 = time - 3600
# print(time2.get_time())

# time3 = time2 - time
# print(time3.get_time())




class Length:
    def __init__(self, *args):
        self.__number = args

    def __len__(self):
        return len(self.__number)

    def __abs__(self):
        return list(map(abs, self.__number))


# lenght = Length(-1,-2,-3,-4,-5,-6,-7,-8,-9,)
# print(len(lenght))
# print(abs(lenght))




class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# aman = Person('Aman')
# print(aman)
# Person('Aman')


class Decorator:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, f = 1, *args, **kwargs):
        print(self.__fn())
        return self.__fn(f)


@Decorator
def return_two(x=2):
    return x
# print(return_two())




class Simvol:
    def __init__(self, simbol):
        self.__simbol = simbol

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент сап болушу керек!')
        return args[0].strip(self.__simbol)

# text = Simvol(' !/? .:;"')
# res = text('  !Hello.!: Привет/')
# print(res)


