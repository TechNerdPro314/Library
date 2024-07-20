Библиотечная система на Python:

Этот проект представляет собой простую систему управления библиотекой, написанную на Python. Она позволяет добавлять, удалять, искать и изменять информацию о книгах в библиотеке.

Функциональные возможности:

1. Добавление книг: Введите название книги, имя автора, год издания и статус ("В наличии" или "Выдана").
2. Удаление книг: Укажите ID книги, которую хотите удалить.
3. Поиск книг: Ищите книги по названию, автору или году издания.
4. Просмотр всех книг: Отображает список всех книг в библиотеке с их ID, названием, автором, годом издания и статусом.
5. Изменение статуса книги: Измените статус книги с "В наличии" на "Выдана" или наоборот.
   
Файлы:

1. library.json: Хранит данные о книгах в формате JSON.
2. main.py: Содержит код для запуска системы.
   
Запуск:

Сохраните код Python как main.py.
Откройте терминал и перейдите в каталог, где находится main.py.
Запустите систему, используя команду python main.py.
Следуйте инструкциям на экране, чтобы использовать функции системы.
Пример использования:

> Добавить книгу
Введите название книги: "Война и мир"
Введите имя автора: "Лев Толстой"
Введите год издания: 1869
Книга добавлена!

> Отобразить все книги
Список всех книг:
ID: 1, Название: "Война и мир", Автор: "Лев Толстой", Год: 1869, Статус: "В наличии"

> Изменить статус книги
Введите ID книги: 1
Введите новый статус (В наличии/Выдана): Выдана
Статус книги изменен!

> Поиск книг
Введите поисковый запрос: мир
Результаты поиска:
ID: 1, Название: "Война и мир", Автор: "Лев Толстой", Год: 1869, Статус: "Выдана"


Примечания:

1. Система использует файл library.json для хранения данных о книгах. Если этот файл не существует, он будет создан автоматически при первом запуске системы.
2. Вы можете изменить код в соответствии с вашими потребностями.
