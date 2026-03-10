# 1
# import math
# x = float(input("1 - sonni kiriting: "))
# y = float(input("2 - sonni kiriting: "))
# a = x + y
# b = math.pow(y, 2)
# c = b + 2
# d = x + math.pow(x, 3) / 5
# e = math.exp(y + 2)
# c1 = a / (b + math.fabs(c / d)) + e
# print("%.2f" % c1)

# import math
# a = float(input("1 - sonni kiriting: "))
# b = float(input("2 - sonni kiriting: "))
# c = math.pow(a, 2) + math.pow(b, 2) + 2
# d = b * (a + b) / (2 * b + a * b)
# t = math.pow(a, 1 / 5) + math.pow(d, 1 / 4) * c 
# print("%.2f" % t)

# import math
# a = int(input("2 - sonni kiriting: "))
# b = int(input("3 - sonni kiriting: "))
# c = int(input("4 - sonni kiriting: "))
# x = float(input("1 - sonni kiriting: "))
# d = 8.2 * math.pow(x, 2)
# z = math.cos(x - 2)
# y = math.fabs(x ** 3 + 3 * x)
# m = math.sqrt(y + z)
# t = a / 4 + b / 3 + c / 2 + 1
# w1 = 0.75 +( d + m ) / t
# print('%.2f' %w1)


# import math
# a = int(input("1-sonni kiriting: "))
# x = float(input("2-sonni kiriting: "))
# b = math.sqrt(x - 1)
# c = math.sqrt(x + 2)
# d = math.log10(math.sqrt(a * math.pow(x, 2)) + 2)
# e = math.sqrt(c + math.sqrt(x + 24) + math.pow(x, 5))
# tt = (b + c + d) / e
# print("%.2f" % tt)

# import math
# a = int(input("1 - sonni kiriting: "))
# x = float(input("2 - sonni kiriting: "))
# b = x * math.sin(x / 2 + x / 3 + x / 4)
# c = math.log10(math.pow(x, 2) - 2) + math.pow(3, a)
# d = math.cos(x + 3) * math.sin(x + 3) + 8
# bb1 = b + c / d
# print(bb1)


# import math 
# a = int(input("1 - sonni kiriting: "))
# x = float(input("2 - sonni kiriting: "))
# y = float(input("3 - sonni kiriting: "))
# b = math.pow(y, 2) + math.exp(x) 
# c = math.sqrt(math.exp(x) + a /( math.pow(x, 2) + 2))
# d = math.pow(math.cos(x), 2) / math.sin(math.pow(x, 2))
# e = math.pow(math.cos(x), 3)
# tt = math.sqrt(b + c + d) + e
# print("%.2f" % tt)

# 20
import math
x = float(input("1 -sonni kiriting: "))
y = float(input("2 -sonni kiriting: "))
a = (math.pow(x, 2) + 1) / (math.pow(x, 2) + (x * y + math.pow(y, 2)) / (math.pow(y, 2) + (y + x * y) / (math.fabs(x * y) + 5)))
b = 1 / (1 + math.cos(x) + (1 / math.sin(math.fabs(x))))
t11 = a + b
print("%.2f" % t11)