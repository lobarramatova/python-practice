# Data types
# 1. integer; 2. float; 3. string; 4.boolean; 5.list; 6. tuple; 7.dictionary

# Dictionary
# key - value pair (kalit-qiymat juftligi)
car = {
    'brand': "Ford" ,
    'name' : "Mustang" ,
    'year': 2000,
    'color': "blue"
}
print( car, type(car))

student = {
    'fullname': 'John Doe',
    'age': 20,
    'course': 3,
    'favourite_books': ['Atomic habits', "O'tkan kunlar", 'Dunyoning ishlari'],
    'is_completed': False,
     'is_married': True
}

# 1. Qiymatlarni olish
print(student['fullname'])
print(student['age'])
print(student['favourite_books'])

for book in student['favourite_books']:
    print(book)

# 2. Qiymatlarni o'zgartirish
student['age'] = 21
student['course'] = 4
print(student)

# 3. Yangi Key - value qo'shish
student['hobbies'] = ['Reading books', 'Watching a football match', 'Learning new things']
print(student)

# 4. Key-value ni o'chirish
del student['is_married']
print(student)

# 5. Empty dict
talaba_1 = {}

talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310' 
} 
 
print(telefonlar.get("vali"))
print(telefonlar.get("akmal")) # none 
