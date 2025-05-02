from abc import ABC, abstractmethod

# SmartComponent.py - Common interface for all components
class SmartComponent(ABC):
    @abstractmethod
    def turn_on(self):
        pass  # Turn on the component
    
    @abstractmethod
    def turn_off(self):
        pass  # Turn off the component

# AirConditioner.py
class AirConditioner(SmartComponent):
    def turn_on(self):
        print("Air Conditioner is now ON.")
    
    def turn_off(self):
        print("Air Conditioner is now OFF.")

# SmartLight.py
class SmartLight(SmartComponent):
    def turn_on(self):
        print("Smart Light is now ON.")
    
    def turn_off(self):
        print("Smart Light is now OFF.")

# CompositeSmartComponent.py - Composite class for groups of components
class CompositeSmartComponent(SmartComponent):
    def __init__(self):
        self.components = []

    def add_component(self, component: SmartComponent):
        self.components.append(component)

    def remove_component(self, component: SmartComponent):
        self.components.remove(component)

    def turn_on(self):
        for component in self.components:
            component.turn_on()

    def turn_off(self):
        for component in self.components:
            component.turn_off()

# SmartHomeController.py - Main controller to demonstrate usage
if __name__ == "__main__":
    # Create individual devices
    air_conditioner = AirConditioner()
    smart_light = SmartLight()

    # Create a room and add devices
    room1 = CompositeSmartComponent()
    room1.add_component(air_conditioner)
    room1.add_component(smart_light)

    # Add more rooms for demonstration
    room2 = CompositeSmartComponent()
    room2.add_component(AirConditioner())
    room2.add_component(SmartLight())

    # Create a floor and add rooms
    floor = CompositeSmartComponent()
    floor.add_component(room1)
    floor.add_component(room2)

    # Create the house and add floors
    house = CompositeSmartComponent()
    house.add_component(floor)

    # Control the entire house
    print("Turning ON all devices in the house:")
    house.turn_on()
    print("\nTurning OFF all devices in the house:")
    house.turn_off()

    # Control a single floor
    print("\nTurning ON all devices on the first floor:")
    floor.turn_on()
    print("\nTurning OFF all devices on the first floor:")
    floor.turn_off()

    # Control a single room
    print("\nTurning ON all devices in Room 1:")
    room1.turn_on()
    print("\nTurning OFF all devices in Room 1:")
    room1.turn_off()
