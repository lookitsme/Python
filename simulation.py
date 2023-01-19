import random

class Car:
    def __init__(self, name, speed, fuel_level, tire_wear):
        self.name = name
        self.speed = speed
        self.fuel_level = fuel_level
        self.tire_wear = tire_wear
        self.distance_traveled = 0
        
    def simulate_pit_stop(self):
        pit_stop_time = random.uniform(5,15)
        self.fuel_level -= 20* pit_stop_time/10
        self.tire_wear -= 30* pit_stop_time/10
        self.speed += 5
        
    def simulate_weather(self):
        wind = random.uniform(-5, 5)
        rain = random.uniform(0, 10)
        temperature = random.uniform(10, 40)
        
        self.speed -= wind * 0.1
        self.speed -= rain * 0.05
        self.tire_wear += rain * 0.1
        self.fuel_level -= (temperature - 20) * 0.01
        
        if self.speed < 0:
            self.speed = 0
            
    def __str__(self):
        return f"{self.name}: {self.distance_traveled} miles Fuel:{self.fuel_level} Tire:{self.tire_wear}"

def simulate_race(cars, laps):
    for i in range(laps):
        for car in cars:
            car.simulate_weather()
            car.distance_traveled += car.speed
            if car.fuel_level <= 0:
                car.simulate_pit_stop()

def display_race(cars):
    for car in cars:
        print(car)
        
if __name__ == "__main__":
    
    cars = [Car("Red Bull", 60, 100, 15), Car("Ferrari", 60, 100, 30), Car("Mercedes", 50, 100, 14), Car("Audi", 50, 100, 20), Car("AlphaTauri", 55, 100, 20), Car("Williams", 60, 100, 20)]
    for car in cars:
        car.total_distance = 0
        car.total_fuel_level = 0
        car.total_tire_wear = 0
    for i in range(100):
        simulate_race(cars, 50)
        for car in cars:
            car.total_distance += car.distance_traveled
            car.total_fuel_level += car.fuel_level
            car.total_tire_wear += car.tire_wear
            car.distance_traveled = 0
            car.fuel_level = 100
            car.tire_wear = 20
            winner = cars[0]
    for car in cars:
        car.average_distance = round(car.total_distance/100,3)
        car.average_fuel_level = round(car.total_fuel_level/100,3)
        car.average_tire_wear = round(car.total_tire_wear/100,3)
        if car.average_distance > winner.average_distance:
            winner = car      
        print(f'{car.name} average distance: {car.average_distance}, average fuel level: {car.average_fuel_level}, average tire wear: {car.average_tire_wear}')
               
    print("")  
    print(f'The winner is {winner.name} with an average distance of {winner.average_distance}')