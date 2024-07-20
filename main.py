import json

def load_data():
    try:
        with open('library.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('library.json', 'w') as f:
        json.dump(data, f, indent=4)

def add_book():
    title = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    year = int(input("Введите год издания: "))

    data = load_data()
    data['books'].append({
        'id': len(data['books']) + 1,
        'title': title,
        'author': author,
        'year': year,
        'status': "В наличии"
    })
    save_data(data)
    print("Книга добавлена!")

def remove_book():
    id = int(input("Введите ID книги: "))

    data = load_data()
    if id in [book['id'] for book in data['books']]:
        for book in data['books']:
            if book['id'] == id:
                data['books'].remove(book)
                save_data(data)
                print("Книга удалена!")
                break
    else:
        print("Книга с таким ID не найдена.")

def search_books():
    term = input("Введите поисковый запрос: ")

    data = load_data()
    results = [book for book in data['books']
               if term.lower() in book['title'].lower() or
               term.lower() in book['author'].lower() or
               str(book['year']) == term]

    if results:
        print("Результаты поиска:")
        for book in results:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("По вашему запросу ничего не найдено.")

def show_all_books():
    data = load_data()

    if data['books']:
        print("Список всех книг:")
        for book in data['books']:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
    else:
        print("В библиотеке нет книг.")

def change_status():
    id = int(input("Введите ID книги: "))
    new_status = input("Введите новый статус (В наличии/Выдана): ")

    data = load_data()
    if id in [book['id'] for book in data['books']]:
        for book in data['books']:
            if book['id'] == id:
                book['status'] = new_status
                save_data(data)
                print("Статус книги изменен!")
                break
    else:
        print("Книга с таким ID не найдена.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книг")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            show_all_books()
        elif choice == '5':
            change_status()
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
