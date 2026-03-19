# Amaliyot
# 1
dictionary = {
    'integer': 'Butun son',
    'if': 'Shartlarni tekshirish operatori',
    'float': "O'nlik son",
    'for': 'Takrorlash operatori',
    'boolean': 'Mantiqiy qiymat'
}
for key, value in sorted(dictionary.items()):
    print(f"{key.title()} - {value}")

# 2
davlatlar = {
    "O'zbekiston": 'Toshkent',
    'Rossiya': 'Moskva',
    'AQSH': 'Vashington',
    'Germaniya': 'Berlin',
    'Fransiya': 'Parij',
    'Italiya': 'Rim',
    'Qirg\'iziston': 'Bishkek',
    'Qozog\'iston': 'Nursulton',    
    'Turkiya': 'Anqara',
    'turkmaniston': 'Ashgabat',
    'ispaniya': 'Madrid'
}
print("Davlatlar")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())
print("\nPoytaxtlar")
for poytaxt in sorted(davlatlar.values()):  
    print(poytaxt.title())

# 3 
# 1 - usul
kalit = input("Qaysi davlatning poytaxtini bilishni istaysiz? ")
if kalit in davlatlar:
    print(f"{kalit.title()}ning poytaxti {davlatlar[kalit].title()}")
else:
    print("Kechirasiz, bizda bu davlat haqida ma'lumot yo'q")

# 2 - usul
if davlatlar.get(kalit) == None:
    print("Kechirasiz, bizda bu davlat haqida ma'lumot yo'q")
else:
    print(f"{kalit.title()}ning poytaxti {davlatlar[kalit].title()}")