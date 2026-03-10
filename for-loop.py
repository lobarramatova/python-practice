# Takrorlanish operatorlari
# loop - sikl
# 1. for loop
# 2. while loop
# students = ['elbek', 'maftuna', "g'ulomjon", 'mahliyo', 'dilbek']
# for student in students:
#     print(student) 


# for guest in students:
#     print(f"hurmatli {guest}, sizni interviewga taklif qilmoqchimiz")

# print("hurmat bilan , Al-Xorazmiy vorislari loyihasi") 

# # sonlar ro'yxati
# even_numbers = list(range(2, 51, 2))
# for number in even_numbers:
#     print(number)
# print('Dastur tugadi.')


# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.") 


# for son in range(11):
#     print(son)

# s = 0
# numbers = [12, 5, 18, 25, 23]
# for number in numbers:
#     print(number)
#     #x+=5 => x = x + 5
#     s += number 
#     print(s) 

# # 1 dan 50 gacha bo'lgan toq sonlar yig'indisi
# summa = 0
# for son in range(1, 50, 2):
#     summa += son
#     print(summa)

# numbers = [12, 5, 18, 25, 23, 88, -52]
# # o'rtacha qiymat = s / length
# s = 0
# for number in numbers:
#     s += number
#     print(s / len(numbers))
 
# 1 dan 20 gacha bo'lgan juft sonlarni o'rta arifmetigini toping
# summa = 0
# for son in range(1, 21, 2):
#     summa += son

# nums = list(range(1, 21, 2))
# avarage_value = summa / len(nums)
# print(avarage_value)

# n!= 1 * 2 * 3 * ... * (n - 1) * n
# k = 1
# for son in range(1, 20):
#     k *= son # k = k * son
# print(k)

# o'rta geometrik 
# import math
# numbers = [12, 5, 18, 25, 23, 88]
# l = len(numbers)
# k = 1
# for number in numbers:
#     k*= number
# a = math.pow(k, 1 / l) 
# print(a)

# s = 0
# k = 1
# for number in range(1, 21):
#     if number % 2 == 0:
#         k *= number
#     else:
#         s += number
# y = k / s
# print(y)

# s = 0   
# counter = 0                                                  
# numbers = [7, 97, -58, 90]
# for number in numbers:
#     if number % 2 == 0:
#         s += number
#         counter += 1

# print(s / counter)

# a = 0
# numbers = [97, 97, -92, 14, 22]
# for number in numbers:
#     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         a += number
# print(a)  

# a = 0
# c = 0
# numbers = [76, 12, 51, 50, 98]
# for number in numbers:
#     if number % 2 == 1:
#         a += number
#         c += 1
# print(a / c)
 
# 122 
# a = 0
# s = 0
# numbers = [44, 59, -75, 73]
# for number in numbers:
#     a += number ** 2
#     s += number
# b = s / len(numbers)
# print(a, b)

# 114
# import math
# numbers = [44, 34, 42, 83, 43, 64]
# a = 1
# for number in numbers:
#     if number % 2 == 0 or number % 5 == 0:
#         a *= number
# b = math.sin(a)
# print(b)

# 115
# numbers = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# m = int(input("m sonini kiriting: "))
# s = 0
# for number in numbers: 
#     if number < m:
#         s += number ** 2
# print(s)

# 126
# import math 
# s = 0
# numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# for number in numbers:
#     s += number
# length = len(numbers)
# b = s / length
# log_value = math.log(b)
# print(b)

# for index in range(0, length):
#     if numbers[index] < 0:
#         numbers[index] = log_value

# print(numbers) 

#127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# a = min(numbers)
# for index in range(0, len(numbers)):
#     if numbers[index] < 0:
#         numbers[index] = a ** 2
# print(numbers)

#123
# numbers = [3, 17, -59]
# s = 0
# for index in range(len(numbers)):
#     if(index + 1) % 2 == 0:
#         s += numbers[index]

# for number in numbers:
#     if number % 2 == 1:
#         print(number / s, " ")
#     else:
#         print(number, " ")

#104
# numbers = [74, 0, 1, 33]
# m = min(numbers)
# for index in range(len(numbers)):
#     if numbers[index] == m:
#         numbers[index], numbers[-1] = numbers[-1], numbers[index]
# print(numbers)
 
#110  
# numbers = [7, 11, 83, 18, 31]
# m = int(input())
# k = int(input())
# s = 1
# for number in numbers:
#     if number == k or number == m:
#         s *= number
# print(s)

# numbers = [74, 0, 1, 33]
# min_value = min(numbers)
# last_element = numbers[-1]
# # print(numbers.index(1)) // 2
# min_index, numbers[-1] = numbers.index(min_value), min_value
# print(*numbers)

# a = 2
# b = 5
#1 - usul
# a,b = b, a
# print(a,b) 

# 2-usul
# c - temporary variable
# c = a
# a = b
# b = c

# 3-usul
# [a, b] = [b, a]
# print(a, b)

# 124
k = int(input())
numbers = [29, 50, -14, 4, 27, -56]
max_value = max(numbers)                           
max_index = numbers.index(max_value)    
numbers[max_index] = numbers[k -1]
numbers[k -1] = max_value
print(numbers)