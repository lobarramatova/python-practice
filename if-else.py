# age = int(input("Yoshingizni kiriting"))
# if age > 18:
#     print("Kirish huquqiga egasiz")
# else: 
#     print("Siz hali yoshsiz")

# ball = int(input("Ballingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'tolmadingiz")
# elif ball >= 56 and ball < 70:
#     print("Siz imtihondan 3 baho bilan o'tdingiz")
# elif ball >= 70 and ball < 86:
#     print("Siz imtihondan 4 baho bilan o'tdingiz")
# elif ball >= 86 and ball <=100:
#     print("Siz imtihondan 5 baho bilan o'tdingiz") 
# else:
#     print("Iltimos, 0 dan 100 gacha ball kiriting")
# age = int(input("Yoshingizni kiriting "))
# if age > 16:
#     print("Pasport olish huquqiga egasiz ")
# else: 
#     print("Siz hali pasport olish huquqiga ega emassiz")


# number = float(input("Istalgan sonni kiriting "))
# if number > 0:
#     print("Siz kiritgan son musbat")
# else: 
#      print("Siz kiritgan son manfiy")   



# number = int(input("Istalgan sonni kiriting "))
# if number % 2 == 0:
#     print("Siz kiritgan son juft")
# else: 
#      print("Siz kiritgan son toq")   

#Amaliyot

# number = int(input("Istalgan sonni kiriting "))
# if number % 2 == 0 and number % 3 == 0:
#     print("Siz kiritgan 6 ga bo'linadi")
# else: 
#      print("Siz kiritgan son 6 ga bo'linmaydi")   


# # 2-mashq
# a = int(input("Uchburchakning 1-tomonini kiriting ")) 
# b = int(input("Uchburchakning 2-tomonini kiriting "))
# c = int(input("Uchburchakning 3-tomonini kiriting "))
# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasash mumkin")
# else: 
#     print("Uchburchak yasash mumkin")

# 3-mashq
# a = int(input("1-sonni kiriting ")) 
# b = int(input("2-sonni kiriting "))
# c = int(input("3-sonni kiriting "))
# if a < b < c:
#     print("YES")
# else:
#     print("NO")

# # 4-mashq
# a = int(input("1-sonni kiriting ")) 
# b = int(input("2-sonni kiriting "))
# if a > b:
#     print(a)
# else: 
#     print(a,b)

# # 5-mashq
# a = int(input("1-sonni kiriting ")) 
# b = int(input("2-sonni kiriting "))
# if a <= b:
#     a = 0
#     print(a,b) 
# else: 
#     print(a,b)

# # 6-mashq
# import math
# a = int(input("1-sonni kiriting ")) 
# b = int(input("2-sonni kiriting "))
# c = int(input("3-sonni kiriting "))
# if a >= b >= c:
#     print(2 * a, 2 * b, 2 * c)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))

# 7-mashq
# x = int(input("1-sonni kiriting ")) 
# y = int(input("2-sonni kiriting ")) 
# a = 2 * x * 2 * y
# b = (x + y) / 2
# if x > y:
#     y = b
#     x = a
# else:
#     x = b
#     y = a

# print( "%.1f" % x, "%.1f" % y)

# # 8- mashq
# import math
# x = float(input("1-sonni kiriting ")) 
# y = float(input("2-sonni kiriting ")) 
# if x < 0 and y < 0:
#     print(math.fabs(x), math.fabs(y))
# elif x < 0 or y < 0:
#     print((x + 0.5), (y + 0.5))
# elif x > 0 and y > 0:
#     print(x, y)

# # 9-mashq
# import math
# a = int(input("1-sonni kiriting ")) 
# b = int(input("2-sonni kiriting "))
# c = int(input("3-sonni kiriting "))
# D = (b ** 2) - (4 * a * c)
# if D < 0:
#     print("NO")
# else: 
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print("%.2f" % x1, "%.2f" % x2)

# # 9-mashq
# import math
# x = float(input("1-sonni kiriting ")) 
# y = float(input("2-sonni kiriting "))
# z = float(input("3-sonni kiriting "))
# if x >= 1 and x <= 3:
#     print(x)
# if y >= 1 and y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)

# # 10-mashq
# x = int(input("1-sonni kiriting ")) 
# y = int(input("2-sonni kiriting "))
# z = int(input("3-sonni kiriting "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2

# print(x, y, z)


# 12.77 , 15 , 18, 0 , -75, 89, 25
# print(max(12.77 , 15 , 18, 0 , -75, 89, 25))
# print(min(12.77 , 15 , 18, 0 , -75, 89, 25))

# x = float(input("1 - sonni kiriting: ")) 
# y = float(input("2 - sonni kiriting: ")) 
# print(max(x, y), min(x, y))

# x = float(input("1 - sonni kiriting: ")) 
# y = float(input("2 - sonni kiriting: ")) 
# z = float(input("3 - sonni kiriting: ")) 
# a = min(x + y / 2, x, y, z)
# print(max(x + y + z, x, y, z), a ** 2) 

# 42 - misol
# a = float(input("1 - sonni kiriting: ")) 
# b = float(input("2 - sonni kiriting: ")) 
# c = float(input("3 - sonni kiriting: ")) 
# d = float(input("4 - sonni kiriting: "))
# x = max(a, b, c, d)
# y = min(a,b,c,d)
# if a <= b <= c <= d:
#     a = b = c = d = x
# else:
#     a = b = c = d = y  
# print(a, b, c, d)

# x = float(input("1 - sonni kiriting: "))
# y = float(input("2 - sonni kiriting: "))
# a = (x + y) / 2
# b = 2 * x * y
# if x > y:
#     x = a
#     y = b
# elif x < y:
#     x = b
#     y = a

# print(x, y)

#41 - misol
x = float(input("1 - sonni kiriting: "))
y = float(input("2 - sonni kiriting: "))
z = float(input("3 - sonni kiriting: "))
if x < 1 and y < 1 and z < 1 and x != y and x != z and y != z:
    a = min(x, y, z)  
    if a == x:
        x = (y + z) / 2
    elif a == y:
        y = (x + z) / 2
    else:
        z = (x + y) / 2

print(x, y, z)
