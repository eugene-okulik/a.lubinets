my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ["hi", "my", 'dear', "friend", '!'],
    'dict': {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'age': 43,
        'country': 'Russia',
        'city': 'Tomsk'
    },
    'set': {44, 55, 12, 67, 88}
}

# вывод последнего элемента в ключе 'tuple'
print(f"Последний элемент в ключе 'tuple': {my_dict['tuple'][-1]}")

# добавил в конец элемнент для ключа 'list'
my_dict['list'].append('Welcome')

# удалил второй элемент в ключе 'list'
my_dict['list'].pop(1)

# добавил элемент с ключом ('i am a tuple')
my_dict['dict']['i am a tuple'] = 'i am not a tuple'

# удалил значение из ключа 'dict'
del my_dict['dict']['age']

# добавил новый элемент в множество
my_dict['set'].add(11)

# удалил элемент из множества
my_dict['set'].remove(55)

# вывод словаря my_dict
for key, value in my_dict.items():
    print(f"{key} : {value}")
