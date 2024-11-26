def read_cook_book(file_name):
    """Читает файл с рецептами и возвращает словарь cook_book."""
    cook_book = {}
    
    with open(file_name, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            
            cook_book[dish_name] = ingredients
            file.readline()
    
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """Создает список покупок на основе выбранных блюд и количества персон."""
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
    return shop_list

if __name__ == "__main__":
    cook_book = read_cook_book('recipes.txt')
    
    print("Кулинарная книга:")
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient}")
        print()
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    
    print("Список покупок:")
    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details}")

