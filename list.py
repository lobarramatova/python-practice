# List - ro'yxat
user1 = "Bekhruz"
user2 = "Maftuna"
print(type(user1))
users = ['Gulyora', "G'ulomjon", "John", 'Margaritta']
# List elementlari indekslari
# Dasturlashda indekslanish 0 dan boshlanadi
# List elementini olish (element indeksi orqali olinadi)
first_element = users[0]
third_element = users[2]
print(first_element, third_element, users[3])
print(type(users))
mixed_data = ['test', 12, True, -5.75, ["hey", 'hi', 'py', 'js', 'c++', 25]] 
# List uzunligi (length of list) - ro'yxatdagi elementlar soni
print(len(users))
print(len(mixed_data)) 
# first_element
print(mixed_data[0])
# last element
length = len(mixed_data)
print(mixed_data[length - 1])
# list elentin o'zgartirish
mixed_data[2] = False
print(mixed_data[2])
# Element qo'shish
users.append('valeriy')
print(users)

users.insert(0, 'Mahliyoxon')
print(users)
users.insert(2, 'Cristiano')  
print(users)
users.insert(len(users) - 1, 'nodir')
print(users)
# Element o'chirish      
del users[4]
print(users)
users.remove('Mahliyoxon')
print(users) 

# Listdan element sug'urib olish
# list.pop(index?)
deletedElement = users.pop(1)
print(deletedElement)
print(users)

lastElement = users.pop()
print(lastElement)
print(users)