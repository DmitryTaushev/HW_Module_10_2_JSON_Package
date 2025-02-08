import pickle
import json

class Stadium:

    def __init__(self, name, seats, year):
        self.name = name
        self.seats = seats
        self.year = year

    def get_name(self):
        return self.name

    def get_seats(self):
        return self.seats

    def get_year(self):
        return self.year

    def stadium_inform(self):
        return f"Стадион {self.name}, построенный в {self.year} году, вмещает {self.seats} кол-во человек"

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

class JSONDataAdapter:

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return json.dumps({
                'name': obj.get_name(),
                'seats': obj.get_seats(),
                'year': obj.get_year(),
                'class': obj.__class__.__name__,
                'methods': {
                    'get_name': obj.get_name(),
                    'get_seats': obj.get_seats(),
                    'get_year': obj.get_year(),
                    'stadium_inform': obj.stadium_inform()
                }
            }, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(obj):
        obj = json.loads(obj)

        try:
            name = obj['name']
            seats = obj['seats']
            year = obj['year']
            stadium = Stadium(name, seats, year)
            return stadium
        except AttributeError:
            print('Неверная структура!')


if __name__ == '__main__':
    stadium = Stadium('Anfield', '61276', '1884')
    print(pickle_object(stadium, 'Stadium_inform.pkl'))
    print(unpickle_object('Stadium_inform.pkl'))
    stadium.stadium_inform()
    print(stadium.stadium_inform())
    stadium_json = JSONDataAdapter.to_json(stadium)
    print(stadium_json)
    stadium_obj = JSONDataAdapter.from_json(stadium_json)
    stadium_obj.stadium_inform()