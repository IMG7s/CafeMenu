

menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}

order={}


# DONE                      --- IGNORE ---
def display_menu():
    print("Cafe Menu:")
    print(f'Отсортированные по названию блюда:')
    for item, price in sorted(menu.items(), key=lambda x: x[0]):
        print(f"{item}: {price} руб.")
    print('\nОтсортированные по цене блюда:')
    for item, price in sorted(menu.items(), key=lambda x: x[1]):
        print(f"{item}: {price} руб.")


# DONE                      --- IGNORE ---
def display_average_price():
    if menu:
        print(f"\nСредняя стоимость: {sum(list(map(lambda x: x[1], menu.items()))) / len(menu)} руб.")
    else: print("Меню пусто.")

# DONE                      --- IGNORE ---
def add_or_update_item():
    item = input("Введите название блюда: ")
    if not item:
        print("Название блюда не может быть пустым. Пожалуйста, попробуйте снова.")
        return add_or_update_item()
    try:
        price = int(input("Введите цену блюда: "))
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return add_or_update_item()

    menu.update({item: price})
    print(f"{item} Добавлено/обновленно {price} руб.")

# DONE                      --- IGNORE ---
def remove_item():
    global menu
    item = input("Блюдо для удаления: ")
    menu.pop(item) if item in menu else print(f"{item} нет в меню.")


# DONE                      --- IGNORE ---
def lowest_selected_price():
    try:
        n=int(input("Число для выбора блюд с наименьшей ценой: "))
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return lowest_selected_price()
    print(f'{[i[0] for i in list(filter(lambda x: x[1]<n, menu.items()))]}')


# DONE                      --- IGNORE ---
def min_max_price():
    if menu:
        print(f'Min price: {min(menu.items(), key=lambda x: x[1])[0]}\n\
              Max price: {max(menu.items(), key=lambda x: x[1])[0]}')
    else: print("Меню пусто.")


# DONE                      --- IGNORE ---
def sorted_by_drinks():
    drinks = sorted({item for item in list(filter(lambda drink: drink[0] in ['coffee', 'tea', 'juice'], menu.items()))},key=lambda x: x[1])
    for item, price in drinks:
        print(f"{item}: {price} руб.")

# DONE                      --- IGNORE ---
def create_oreder():
    global order
    order = {}
    ordered_items = input('Введите через запятую блюда, которые хотите заказать: ').replace(' ', '').split(',')
    if not all(item in menu for item in ordered_items):
        print("Одно или несколько блюд отсутствуют в меню. Пожалуйста, попробуйте снова.")
        return create_oreder()
    order.update({item: menu[item] for item in ordered_items})
    print(f'{order}')

# DONE                      --- IGNORE ---
def total_order_price():
    from functools import reduce
    if not order:
        print("Заказ пуст. Пожалуйста, создайте заказ сначала.")
        return
    return reduce(lambda x, y: x+y, list(map(lambda x: x[1], order.items())))

# DONE                      --- IGNORE ---
def display_ordered_items():
    if not order:
        print("Заказ пуст. Пожалуйста, создайте заказ сначала.")
        return
    for i, (item, price) in enumerate(order.items(), start=1):
        print(f"{i}. {item} — {price} руб.")
    print(f'Итого: '); total_order_price()

# DONE                      --- IGNORE ---
def check_order():
    if any(order) == False: print('Вы ничего не выбрали'); return
    if total_order_price() > 500: print('Поздравляем, у вас скидка 10%!')


# Для проверки функций:

# display_menu()
# display_average_price()
# add_or_update_item()
# remove_item()
# lowest_selected_price()
# min_max_price()
# sorted_by_drinks()
# create_oreder()
# print(total_order_price())
# display_ordered_items()
# check_order()

