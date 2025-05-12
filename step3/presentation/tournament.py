from race_tools import race_time, scoreboard

class Tournament(Car, Race):
    def __init__(self, cars, races):
        self.cars = cars
        self.races = races


    def run_race(self, race):
        results = []
        for car in self.cars:
            time = race_time(car.zero_to_100, car.top_speed, race.distance)   #time = race_time(car['zero_to_100'], car['top_speed'], race['distance'])
            results.append((car.model, time))   #results.append((car['model'], time))
        results.sort(key=lambda x: x[1])  # Sort by race time
        return results

    def print_results(self):
        for i, race in enumerate(self.races):
            results = self.simulate_race(race)
            print(f"Race {i+1} at {race['location']}:")
            print(f"Winner: {results[0][0]}")
            print(f"Runner-up: {results[1][0]}")
            print(f"Third place: {results[2][0]}")
            print("The rest: " + ", ".join([car[0] for car in results[3:]]))
            print()

# Example usage:
# Adding cars
car1 = {'model': "Model S", 'manufacturer': "Tesla", 'zero_to_100': 2.4, 'top_speed': 250}
car2 = {'model': "Mustang", 'manufacturer': "Ford", 'zero_to_100': 3.5, 'top_speed': 240}
car3 = {'model': "Civic", 'manufacturer': "Honda", 'zero_to_100': 4.2, 'top_speed': 220}
car4 = {'model': "Corolla", 'manufacturer': "Toyota", 'zero_to_100': 4.5, 'top_speed': 210}

cars = [car1, car2, car3, car4]

# Adding races
race1 = {'location': "Nuremberg", 'distance': 500}
race2 = {'location': "Munich", 'distance': 300}

races = [race1, race2]

# Creating a tournament and printing results
tournament = Tournament(cars, races)
tournament.print_results()
