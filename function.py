# Function - ma'lum vazifani bajaruvchi kod bloklari
# Funksiya yaratish uchun def kalit so'zidan foydalanamiz
# Pythondagi tayyor funksiyalar: print(), input(), len(), range() va boshqalar
print("Hello, World!")
# Funksiayni e'lon qilish(declaration)
def salom_ber():
    print("Salom, dunyo!")

# Funksiayni chaqirish(call)
salom_ber()

# funksiya parametrlar, argumentlar
def salom_ber(ism):
    print(f"Assalomu alekum, {ism}!")

salom_ber("Ali")
salom_ber("Vali")

def yigindi(a, b):
    print(a + b)

yigindi(7, 8)
yigindi(10, 20)

def calculate_age(birth_year, name):
    age = 2026 - birth_year
    print(f"{name}ning yoshi {age}")

calculate_age(1990, "Ali")
calculate_age(1985, "Vali")
# calculate_age()

# Amaliyot
# 4
def solishtirish(a, b):
    if a > b:
        print(f"{a} katta {b} dan")
    elif a < b:
        print(f"{a} kichik {b} dan")
    else:
        print(f"{a} va {b} teng")

solishtirish(5, 10)
solishtirish(20, 15) 
solishtirish(7, 7)