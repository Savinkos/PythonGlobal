def get_name(doc_number):
    """
    Функция возвращает имя человека по номеру документа.
    Если документа нет, возвращает сообщение об ошибке.
    """
    for document in documents:
        if document["number"] == doc_number:
            return document["name"]
    return "Документ не найден"

def get_directory(doc_number):
    """
    Функция возвращает номер полки, на которой находится документ.
    Если документа нет, возвращает сообщение об ошибке.
    """
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
    """
    Функция добавляет новый документ в каталог и перечень полок.
    """
    # Проверим, существует ли указанная полка
    if str(shelf_number) not in directories:
        return f"Полка {shelf_number} не существует"

    # Добавляем документ в список документов
    documents.append({"type": document_type, "number": number, "name": name})

    # Добавляем номер документа на указанную полку
    directories[str(shelf_number)].append(number)
    return f"Документ добавлен на полку {shelf_number}"

# Исходные данные
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# Тестируем функции
if __name__ == '__main__':
    print(get_name("10006"))  # Аристарх Павлов
    print(get_directory("11-2"))  # 1
    print(get_name("101"))  # Документ не найден
    print(add('international passport', '311 020203', 'Александр Пушкин', 3))  # Документ добавлен на полку 3
    print(get_directory("311 020203"))  # 3
    print(get_name("311 020203"))  # Александр Пушкин
    print(get_directory("311 020204"))  # Полки с таким документом не найдено
