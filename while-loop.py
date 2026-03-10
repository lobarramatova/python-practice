# # while loop
# for son in range(1,10):
#     print(son)

#     son = 1
#     while son < 10:
#         print(son)
#         son += 1 # Infinity loop


# Infinity loop - cheksiz sikl / abadiy sikl
# while True:
#    print("Infinity loop")

# while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
#     else:
#         print("Dastur ishlashdan to'xtadi")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
        

# # break operatori
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tsikl to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = 'Istalgan son kiriting'
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break 
#     else:
#         print(float(qiymat) ** 2)

# continue(davom qilish) operatori
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tsikl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# Abadiy sikl tuzog'i 

# Amaliyot - 1
savol = "Yaxshi ko'rgan kitobingizni kiriting"
savol += "(dasturni to'xtatish uchun 'stop' deb yozing): "
qiymat = ''
while qiymat != 'stop':
    qiymat = input(savol)
    if qiymat != 'stop':
        print(qiymat)
    else:
        print("Dastur ishlashdan to'xtadi")
