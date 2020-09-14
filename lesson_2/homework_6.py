'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
'''

shop_items = []
input_digit_error = 'Please use only whole numbers!\n'

shop_items_quantity = 3
counter = 1

while counter <= shop_items_quantity:

    item_name = input('Add product #' + str(counter) + ' name:\n')

    item_price = input('Add product #' + str(counter) + ' price:\n')
    while not item_price.isdigit():
        item_price = input(input_digit_error + 'Add product #' + str(counter) + ' price:\n')
    item_price = int(item_price)

    item_quantity = input('Add product #' + str(counter) + ' quantity:\n')
    while not item_quantity.isdigit():
        item_quantity = input(input_digit_error + 'Add product #' + str(counter) + ' quantity:\n')
    item_quantity = int(item_quantity)

    item_quantity_type = input('Add product #' + str(counter) + ' quantity type:\n')

    shop_items.append((int(counter), {
        'name': item_name,
        'price': item_price,
        'quantity': item_quantity,
        'quantity_type': item_quantity_type
    }))
    counter += 1

print('SHOP PRODUCTS LIST:\n' + str(shop_items))

analytics = {
    'name': [],
    'price': [],
    'quantity': [],
    'quantity_type': []
}

for item in shop_items:
    analytics['name'].append(item[1]['name'])
    analytics['price'].append(item[1]['price'])
    analytics['quantity'].append(item[1]['quantity'])
    analytics['quantity_type'].append(item[1]['quantity_type'])

print('SHOP PRODUCTS ANALYTICS:\n' + str(analytics))

