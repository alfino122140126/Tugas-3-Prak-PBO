from abc import ABC, abstractmethod

class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name
        self.water_needs = water_needs
        self.fertilizer_needs = fertilizer_needs

    @abstractmethod
    def grow(self):
        pass

    def calculate_needs(self, rainfall, soil_moisture):
        if rainfall > 5:
            self.water_needs = max(0, self.water_needs - (rainfall * 0.5))
        if soil_moisture < 50:
            self.fertilizer_needs += 1

    def show_needs(self):
        print(f"Adjusted Water Needs: {self.water_needs} liters")
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg")

class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 5)

    def grow(self):
        print("Rice is growing in the paddy field")

class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)

    def grow(self):
        print("Corn is growing in the farm")

rice = RicePlant()
corn = CornPlant()

rainfall = 10
soil_moisture = 75

rice.grow()
print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
rice.calculate_needs(rainfall, soil_moisture)
rice.show_needs()

print()

rainfall = 2
soil_moisture = 40

corn.grow()
print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
corn.calculate_needs(rainfall, soil_moisture)
corn.show_needs()