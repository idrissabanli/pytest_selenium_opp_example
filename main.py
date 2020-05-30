
class Car():
    wheel_count = 4
    door_count = 4

    def __init__(self, make_, model_, year_, color_): # constructor
        print('init methodu ise dusdu')
        self.make = make_
        self.model = model_
        self.year = year_
        self.color = color_
        print(f"{self.make} yaradildi")

    def start(self):
        print('Masin ise dusdu')
    
    def move(self, distance):
        print(f'{self.make} teker sayi:', self.wheel_count)
        print(f'Masin {distance}km hereket etdi')


class BMW(Car):

    def start(self):
        print('BMW classinin start funksiyasi ise dusdu')
        super().start()


bmw750i = BMW(make_='BMW', model_='750i', year_=2019, color_='black')

bmw750i.start()
bmw750i.move(15)

audi = Car('Audi', color_='red', model_='A5', year_=2019)
audi.start()
audi.move(50)
# print('masinlarin rengi', bmw750i.color, audi.color)