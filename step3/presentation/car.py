# car.py

from datetime import date
from race_tools import race_time, scoreboard

class Car:
    cars = []
    def __init__(self, model, manufacturer, top_speed):
        self.model = model
        self.manufacturer = manufacturer
        self.top_speed = top_speed

    def list_car(self):
        car_info = {
        'model': self.model,
        'manufacturer': self.manufacturer, 
        'top_speed': self.top_speed 
        }
        Car.cars.append(car_info)

    @classmethod
    def tell_cars_info(cls):
        return cls.cars

    @staticmethod
    def virage():
        return "\n/ / / / / V ii//////\n"  

    def __str__(self):
        """Returns a human readable string representation of the car."""
        return f"{self.model} from ({self.manufacturer}) - top_speed: {self.top_speed} km/h"

    def __repr__(self):
        """Returns a string representation that can be used to recreate the car object."""
        return f"Car('{self.model}', '{self.manufacturer}', {self.top_speed})"

class Race:
    races = []
    total_race = 0
    def __init__(self, location, distance):
        self.location = location
        self.distance = distance
        Race.total_race += 1
        self.race_number = Race.total_race


    def list_race(self):
        race_info = {
        'Race': self.race_number,
        'location': self.location,
        'distance': self.distance
        }
        Race.races.append(race_info)

    @classmethod
    def tell_races_info(cls):
        return cls.races


    def __str__(self):
        return f"Race {self.race_number}: {self.location}, {self.distance} km"

    def __repr__(self):
        return f"Race('{self.location}', {self.distance})"


class Tournament(Car, Race):
    race_result = []
    outcome = ""    
    def __init__(self, name, year, cars= Car.cars, races= Race.races):      
        self.cars = cars
        self.races = races
        self.__name = name
        self.__year = year

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name 

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 2020 or value > date.today().year:
            raise ValueError("Year must be between 2020 and current year")
        elif value == date.today().year:
            self.__year = date.today() 
        else:
            self.__year = value
        return self.__year


    def run_race(self):

        for race in self.races:            
            for car in self.cars:             
                time = race_time(car['top_speed'], race['distance'])  
                Tournament.race_result.append((car['model'], time))
                Tournament.race_result.sort(key=lambda x: x[1])  # Sort by race time

            Tournament.outcome += f"Race {race['location']} {race['distance']} km;"
            
            for tup in Tournament.race_result:
                Tournament.outcome += f' {tup[0]} -' 
            Tournament.outcome += '; '
            print(f"result of Race {race['Race']}:\n",Tournament.race_result)
            Tournament.race_result = []
    
    @classmethod
    def report(cls):
        return cls.outcome

    @classmethod
    def display_scoreboard(cls):
        display = scoreboard(cls.outcome)
        return display

#####################...running...########################
