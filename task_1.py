import pickle
import json

class Car:

    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def all_inform(self):
        return f"Автомобиль марки {self.brand}, модель {self.model},{self.year} года"

def pickle_car(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def unpickle_car(filename):
    try:
        with open(filename, 'rb') as file:
            pickle.load(file)
        return "Данные загружены"
    except FileNotFoundError:
        return "Файл не найден!"

class JSONDataAdapter:

    @staticmethod
    def to_json(obj):
        if isinstance(obj, Car):
            return json.dumps({
                'brand': obj.brand,
                'model': obj.model,
                'year': obj.year,
                'class': obj.__class__.__name__,
                'methods': {
                    'get_brand': obj.get_brand(),
                    'get_model': obj.get_model(),
                    'get_year': obj.get_year(),
                    'all_inform': obj.all_inform(),
                }
            }, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(obj):
        obj = json.loads(obj)

        try:
            brand = obj['brand']
            model = obj['model']
            year = obj['year']
            car = Car(brand,model, year)
            return car
        except AttributeError:
            print('Неверная структура!')


if __name__ == '__main__':
    car = Car('Toyota', 'Avensis', '2008')
    pickle_car(car,'car.pkl')
    print(unpickle_car('car.pkl'))
    car_json = JSONDataAdapter.to_json(car)
    print(car_json)
    car_obj = JSONDataAdapter.from_json(car_json)
    car_obj.all_inform()
