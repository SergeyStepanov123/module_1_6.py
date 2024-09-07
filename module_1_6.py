my_dict = {'Sergey': 1991, 'Galyna': 1986, 'Katya': 1995}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Saha'))
my_dict.update({'Lena': 1927, 'Alexey': 1975})
print(my_dict.pop('Galyna'))
print(my_dict)


my_set = {'car', 1997, 12.5, 1997}
print(my_set)

my_set.update([6, 'door'])
print(my_set)
my_set.discard(12.5)
print(my_set)
