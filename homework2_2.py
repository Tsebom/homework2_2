import json, yaml
from pprint import pprint

########################################################################################
# Примерный словарь
#cook_book = {
#  'яичница': [
#    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#    ],
#  'стейк': [
#    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#    ],
#  'салат': [
#    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#    ]
#}

# Записываем примерный словарь в JSON
#def cook_book_json(dictionery):
#  with open('data_file.json', 'w', encoding = 'utf-8') as file:
#    json.dump(dictionery, file, indent = 2, ensure_ascii = False)

#cook_book_json(cook_book)

# Записываем примерный словарь в YAML
#def cook_book_yaml(dictionery):
#  with open('data_file.yml', 'w', encoding = 'utf-8') as file:
#    yaml.dump(dictionery, file, allow_unicode = True)

#cook_book_yaml(cook_book)
#######################################################################################
# Рецепты из JSON
def read_cook_book_json():
  with open('data_file.json', encoding = 'utf-8') as file:
    cook_book = json.load(file)
  return cook_book

# Рецепты из YAML
def read_cook_book_yaml():
  with open('data_file.yml', encoding = 'utf-8') as file:
    cook_book = yaml.load(file)
  return cook_book

# Выбираем фаил JSON или YAML
def select_file():
  file = input('Укажите тип фаила(json/yaml): ')
  file = file.strip()
  file = file.lower()
  if file == 'json':
    return read_cook_book_json()
  if file == 'yaml':
    return read_cook_book_yaml()

# Принуждаем пользователя к правильному вводу типа фаила
def true_type():
  file = select_file()
  while file == None:
    print('Неверный тип фаила! Побруйте еще раз:')
    file = select_file()
  return file

# ДЗ к лекции 2.1 «Открытие и чтение файла, запись в файл»
def get_shop_list_by_dishes(dishes, person_count):
      cook_book = true_type()
      shop_list = {}
      for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
      return shop_list

def print_shop_list(shop_list):
      for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                                shop_list_item['measure']))

def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)

create_shop_list()