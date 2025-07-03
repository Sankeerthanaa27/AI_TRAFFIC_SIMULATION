import time
import random

class Simulation:
    def __init__(self):
        self.directions = ['North', 'East', 'West', 'South']
        self.vehicles = {d: 0 for d in self.directions}

    def generate_traffic(self):
        for direction in self.directions:
            self.vehicles[direction] = random.randint(0, 20)

    def get_max_traffic_direction(self):
        return max(self.vehicles, key=self.vehicles.get)

    def display_signals(self, green_direction):
        print("\n[Traffic Light Status]")
        for direction in self.directions:
            color = "GREEN" if direction == green_direction else "RED"
            print(f"{direction}: {color} (Vehicles: {self.vehicles[direction]})")
        print("\n-----------------------------\n")

    def runSimulation(self):
        print("[INFO] Starting traffic simulation...")
        for i in range(5):  # Simulate for 5 cycles
            print(f"[Cycle {i+1}]")
            self.generate_traffic()
            green = self.get_max_traffic_direction()
            self.display_signals(green)
            time.sleep(2)
