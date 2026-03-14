# Amaliyot
# 1
otam = {'ismi':'Mavlutdin', 't_yil':1954,'viloyat':'Samarqand'}
t_yil = otam['t_yil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi']}, {t_yil}-yilda, {vil} viloyatida tug'ilgan")

# 2
taomlar = {
    "hasan":"osh",
    'husan':'shashlik',
    'ali': 'osh'}
print(f"Ali {taomlar['ali']} ni yaxshi ko'radi")

# 3
python_dictionary = {
    'integer':"Butun son",
    'string':"Matn",
    'tuple':"O'zgarmas ro'yxat",
    'list':"Ro'yxat",
    'float':"O'nlik son",
    }
print(python_dictionary['float'])

# 4
text = input("Kalit so'zni kiriting:")
print(python_dictionary.get(text))
if text in python_dictionary:
    print(python_dictionary[text])
else:
    print("Bunday kalit mavjud emas")

