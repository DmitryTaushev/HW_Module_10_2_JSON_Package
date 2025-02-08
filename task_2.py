import pickle
import json

class Book:

    def __init__(self, author,name,price):
        self.author = author
        self.name = name
        self.price = price

    def get_author(self):
        return self.author

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def book_inform(self):
        return f"Автор {self.author}, книги {self.name}, цена {self.price}"

def pickle_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)
        return "Данные сохранены в файл"


def unpickle_object(filename):
    try:
        with open(filename, 'rb') as file:
            pickle.load(file)
        return "Данные загружены"
    except FileNotFoundError:
        return "Файл не найден!"

class BookEncoder(json.JSONEncoder):

    def default(self, o):
        return {
            "Author": o.author,
            "Name": o.name,
            "Price": o.price,
            "Methods": {
                "get_author": o.get_author(),
                "get_name": o.get_name(),
                "get_price": o.get_price(),
                "book_inform": o.book_inform()
            },
            "ClassName": o.__class__.__name__
        }


if __name__ == '__main__':

    book = Book("Пелевин В.О.", 'Generation <<П>>', '1000')
    book.book_inform()
    print(pickle_object(book, 'book.pkl'))
    print(unpickle_object('book.pkl'))
    json_book = json.dumps(book, cls=BookEncoder, ensure_ascii=False, indent=4)
    print(json_book)
    python_book = json.loads(json_book)
    print(python_book)

    with open(r'my_book_encode.json', 'w', encoding='utf-8') as fp:
        json.dump(book, fp, cls=BookEncoder, ensure_ascii=False, indent=4)

    with open(r'my_book_encode.json', 'r', encoding='utf-8') as fh:
        python_book_from_file = json.load(fh)
    print(python_book_from_file)