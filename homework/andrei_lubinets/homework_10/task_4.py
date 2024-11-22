PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

changed_price_list = PRICE_LIST.split('\n')
names = [line.split()[0] for line in changed_price_list]
prices = [int(line.split()[1].replace('р', '')) for line in changed_price_list]
price_dict = dict(zip(names, prices))
print(price_dict)
